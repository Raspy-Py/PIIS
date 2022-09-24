#include "App.h"
#include "imgui_demo.h"

App::App()
{
    window = std::make_unique<sf::RenderWindow>(sf::VideoMode(800, 800), "Lab_1(Path finding)");
    ImGui::SFML::Init(*window.get());
    ImGui::GetIO().ConfigFlags |= ImGuiConfigFlags_DockingEnable;

    // Add all SFML drawable objects
    SFMLDrawables.push_back(std::make_unique<Maze>(window->getSize(), 10));
}

App::~App()
{
    ImGui::SFML::Shutdown();
}

int App::Run()
{
    while (window->isOpen())
    {
        int code = Tick();
        if (code)
        {
            return code;
        }     
    } 

    return 0;
}

int App::Tick()
{
    // Poll events
    while (window->pollEvent(event))
    {
        ImGui::SFML::ProcessEvent(event);
        if (event.type == sf::Event::Closed)
            window->close();
    }

    // Update
    UpdateImGuiStuff();
    UpdateSFMLStuff();

    // Draw
    window->clear();
    DrawSFMLStuff();
    DrawImGuiStuff();
    window->display();

    return 0;
}

void App::UpdateImGuiStuff()
{
    ImGui::SFML::Update(*window.get(), clock.restart());

    ImGui::Begin("Setting");
    ImGui::Text("Settings will be placed here");
    ImGui::End();

    ImGui::ShowStackToolWindow();
}

void App::UpdateSFMLStuff()
{
    for (auto& entity : SFMLDrawables)
    {
        entity->Update(*window.get());
    }
}

void App::DrawSFMLStuff()
{
    for (auto& entity : SFMLDrawables)
    {
        entity->Draw(*window.get());
    }
}

void App::DrawImGuiStuff()
{
    ImGui::SFML::Render(*window.get());
}

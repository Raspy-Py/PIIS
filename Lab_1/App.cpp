#include "App.h"

App::App()
{
    window = std::make_unique<sf::RenderWindow>(sf::VideoMode(800, 800), "Lab_1(Path finding)");
    ImGui::SFML::Init(*window.get());
    ImGui::GetIO().ConfigFlags |= ImGuiConfigFlags_DockingEnable;
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
    ImGui::SFML::Update(*window.get(), clock.restart());
    UpdateImGuiStuff();
    UpdateSFMLStuff();
    // Draw
    window->clear();
    DrawSFMLStuff();
    ImGui::SFML::Render(*window.get());
    window->display();

    return 0;
}

void App::UpdateImGuiStuff()
{
}

void App::UpdateSFMLStuff()
{
}

void App::DrawSFMLStuff()
{
}

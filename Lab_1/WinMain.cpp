#include "imgui.h"
#include "imgui-SFML.h"
#include "imgui_demo.h"

#include "WinApiNoCrap.h"

#include <SFML/Graphics.hpp>


int WINAPI WinMain(
	_In_ HINSTANCE hInstance,
	_In_opt_ HINSTANCE hPrevInstance,
	_In_ LPSTR lpCmdLine,
	_In_ int nCmdShow
)
{
    sf::RenderWindow window(sf::VideoMode(800, 800), "SFML works!");
    ImGui::SFML::Init(window);
    ImGui::GetIO().ConfigFlags |= ImGuiConfigFlags_DockingEnable;

    int circleDots = 30;
    float radius = 100.0f;
    sf::CircleShape shape(100.f, circleDots);
    shape.setFillColor(sf::Color::Cyan); shape.setPosition(400, 400);

    bool bDrawCircle = true;
    sf::Clock deltaClock;
    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            ImGui::SFML::ProcessEvent(event);
            if (event.type == sf::Event::Closed)
                window.close();
        }
        ImGui::SFML::Update(window, deltaClock.restart());

        /*ImGui::Begin("Window title");
        ImGui::Text("Just some random text");
        ImGui::Checkbox("Draw the circle", &bDrawCircle);
        ImGui::End();

        ImGui::Begin("Window title1");
        ImGui::SliderInt("Points", &circleDots, 3, 30);
        ImGui::SliderFloat("Radius", &radius, 100.0f, 300.0f, "%.2f px");
        ImGui::End();*/

        ImGui::ShowDemoWindow();

        shape.setPointCount(circleDots);
        shape.setRadius(radius);
        shape.setOrigin(radius, radius);

        window.clear();
        if (bDrawCircle)
            window.draw(shape);
        ImGui::SFML::Render(window);
        window.display();
    }

    ImGui::SFML::Shutdown();
    return 0;
}

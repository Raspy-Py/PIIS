#pragma once
// STL
#include <memory>
#include <vector>
// Third party
#include "imgui.h"
#include "imgui-SFML.h"
#include <SFML/Graphics.hpp>
// My modules
#include "Drawable.h"
#include "Maze.h"

class App
{
public:
	App();
	~App();

	int Run();
private:
	int Tick();

	void UpdateImGuiStuff();
	void UpdateSFMLStuff();
	void DrawSFMLStuff();
	void DrawImGuiStuff();
private:
	std::unique_ptr<sf::RenderWindow> window;
	std::vector<std::unique_ptr<Drawable>> SFMLDrawables;
	sf::Clock clock;
	sf::Event event;
};


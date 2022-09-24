#pragma once
#include <SFML/Graphics.hpp>
#include "Drawable.h"

class PathFinder;

class Maze : public Drawable
{
public:
	enum class Cell
	{
		Start,
		Finish,
		CheckPoint,
		Visited,
		Locked,
		None
	};
public:
	Maze(const sf::Vector2u& size, int rows, int cols = -1);

	void SetRows(int rows);
	void SetCols(int cols);
	void SetSize(const sf::Vector2u& size);
	const sf::Vector2u& GetSize();

	void Update(sf::RenderWindow& window) override;
	void Draw(sf::RenderWindow& window) const override;

	void AddCheckPoint(const sf::Vector2u& point);

private:
	int rows;
	int cols;
	sf::Vector2u size;
	sf::Vector2u start;
	sf::Vector2u finish;
	std::vector<sf::Vector2u> checkpoints;
	std::vector<std::vector<Cell>> grid;
	
	void RebuildGrid();
	void PickNextPoint();

private:
	// Drawable parts;
	sf::VertexArray gridLines;
	sf::VertexArray gridCells;
};


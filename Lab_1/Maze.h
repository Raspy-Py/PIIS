#pragma once
#include <SFML/Graphics.hpp>
#include "Drawable.h"

class Maze : public Drawable
{
public:
	enum class Cell
	{
		Start,
		Finish,
		CheckPoint,

	};
public:
	Maze(const sf::Vector2i& size, int rows, int cols = -1);

	void SetRows(int rows);
	void SetCols(int cols);
	void SetSize(const sf::Vector2i& size);
	const sf::Vector2i& GetSize();

	void Update(const sf::RenderWindow& window) override;
	void Draw(const sf::RenderWindow& window) const override;

	void AddCheckPoint(sf::Vector2i point);

private:
	int rows;
	int cols;
	sf::Vector2i size;
	sf::Vector2i start;
	sf::Vector2i finish;
	std::vector<sf::Vector2i> checkpoints;
	std::vector<std::vector<Cell>> grid;
	
	void RebuildGrid();
	void PickNextPoint();
};


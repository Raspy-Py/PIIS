#include "Maze.h"


static const sf::Color DefaultCellColor(100, 100, 100);
static const sf::Color GridLineColor(255, 255, 255);

Maze::Maze(const sf::Vector2u& size, int rows, int cols)
	:
	size(size), rows(rows), cols(cols)
{
	if (cols == -1) this->cols = rows;

	gridLines.setPrimitiveType(sf::Lines);
	gridCells.setPrimitiveType(sf::Quads);

	RebuildGrid();
}

void Maze::RebuildGrid()
{
	gridCells.clear();
	gridLines.clear();

	float hStep = size.x / rows;
	float vStep = size.y / cols;

	for (int i = 1; i < rows; ++i)
	{
		gridLines.append({ sf::Vector2f(0,		i * vStep),GridLineColor });
		gridLines.append({ sf::Vector2f(size.x,	i * vStep),GridLineColor });
	}

	for (int j = 1; j < cols; ++j)
	{
		gridLines.append({ sf::Vector2f(j * hStep,0),		GridLineColor });
		gridLines.append({ sf::Vector2f(j * hStep,size.y),	GridLineColor });
	}

	for (int i = 0; i < rows; i++)
	{
		for (int j = 0; j < cols; ++j)
		{
			gridCells.append({ sf::Vector2f((j) * hStep,		(i) * vStep),		DefaultCellColor });
			gridCells.append({ sf::Vector2f((j + 1) * hStep,	(i) * vStep),		DefaultCellColor });
			gridCells.append({ sf::Vector2f((j + 1) * hStep,	(i + 1) * vStep),	DefaultCellColor });
			gridCells.append({ sf::Vector2f((j) * hStep,		(i + 1) * vStep),	DefaultCellColor });
		}
	}
}

void Maze::PickNextPoint()
{
}

void Maze::SetRows(int rows)
{
}

void Maze::SetCols(int cols)
{
}

void Maze::SetSize(const sf::Vector2u& size)
{
}

const sf::Vector2u& Maze::GetSize()
{
	return size;
}

void Maze::Update(sf::RenderWindow& window)
{
}

void Maze::Draw(sf::RenderWindow& window) const
{
	window.draw(gridCells);
	window.draw(gridLines);
}

void Maze::AddCheckPoint(const sf::Vector2u& point)
{
}

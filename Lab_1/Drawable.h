#pragma once
#include <SFML/Graphics.hpp>

class Drawable
{
public:
	virtual void Update(sf::RenderWindow& window) = 0;
	virtual void Draw(sf::RenderWindow& window) const = 0;
};


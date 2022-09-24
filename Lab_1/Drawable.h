#pragma once
#include <SFML/Graphics.hpp>

class Drawable
{
public:
	virtual void Update(const sf::RenderWindow& window) = 0;
	virtual void Draw(const sf::RenderWindow& window) const = 0;
};


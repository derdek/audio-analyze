from src.db import Session
from src.models.category import Category, CategoryPoint


def create_categories_and_points():
    session = Session()

    category_visa = Category(title="Visa and Passport Services")
    category_diplomatic = Category(title="Diplomatic Inquiries")
    category_travel = Category(title="Travel Advisories")
    category_consular = Category(title="Consular Assistance")
    category_trade = Category(title="Trade and Economic Cooperation")

    category_visa.points = [
        CategoryPoint(point="visa"),
        CategoryPoint(point="passport"),
        CategoryPoint(point="visa application"),
        CategoryPoint(point="passport renewal"),
        CategoryPoint(point="visa renewal"),
        CategoryPoint(point="visa extension"),
    ]

    category_diplomatic.points = [
        CategoryPoint(point="diplomatic"),
        CategoryPoint(point="diplomatic inquiry"),
        CategoryPoint(point="diplomatic mission"),
        CategoryPoint(point="diplomatic relations"),
        CategoryPoint(point="diplomatic immunity"),
    ]

    category_travel.points = [
        CategoryPoint(point="travel advisory"),
        CategoryPoint(point="travel warning"),
        CategoryPoint(point="travel alert"),
        CategoryPoint(point="travel ban"),
        CategoryPoint(point="travel restriction"),
    ]

    category_consular.points = [
        CategoryPoint(point="consular"),
        CategoryPoint(point="consular assistance"),
        CategoryPoint(point="consular services"),
        CategoryPoint(point="consular mission"),
        CategoryPoint(point="consular protection"),
    ]

    category_trade.points = [
        CategoryPoint(point="trade"),
        CategoryPoint(point="trade agreement"),
        CategoryPoint(point="trade cooperation"),
        CategoryPoint(point="trade mission"),
        CategoryPoint(point="trade partnership"),
    ]
    session.add(category_visa)
    session.add(category_diplomatic)
    session.add(category_travel)
    session.add(category_consular)
    session.add(category_trade)
    session.commit()


if __name__ == '__main__':
    create_categories_and_points()

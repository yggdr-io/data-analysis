import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.ticker import FuncFormatter

POUNDS_TO_KG = 2.20462


def get_vehicle_prices_per_kg(
    vehicles: dict[str, tuple[float, float]],
) -> dict[str, float]:
    return {
        name: price / weight * POUNDS_TO_KG
        for name, (price, weight) in vehicles.items()
    }


def get_cheese_prices_per_kg(cheeses: dict[str, float]) -> dict[str, float]:
    return {
        name: price * POUNDS_TO_KG
        for name, price in cheeses.items()
    }


def create_price_dataframe(items: dict[str, float], category: str) -> pd.DataFrame:
    """Create a DataFrame for items with their prices and category."""
    return pd.DataFrame.from_dict(
        {
            "Item": list(items.keys()),
            "Price": list(items.values()),
            "Category": [category] * len(items),
        }
    )


def dollar_formatter(x: float, pos: int) -> str:
    """Formatter for x-axis ticks to display prices in dollar format."""
    if x >= 1:
        return f"${int(x):,}"
    else:
        return f"${x:.2f}"


def plot_price_comparison(vehicle_prices: dict[str, float], cheese_prices: dict[str, float]) -> None:
    """Plot a comparison bar chart of price per pound for vehicles and cheeses."""

    vehicle_df = create_price_dataframe(vehicle_prices, "Vehicle")
    cheese_df = create_price_dataframe(cheese_prices, "Cheese")

    combined_df = pd.concat([vehicle_df, cheese_df], ignore_index=True)
    filtered_df = combined_df[combined_df["Price"] <= 400]

    plt.figure(figsize=(16, 20))
    sorted_df = filtered_df.sort_values("Price", ascending=False)

    palette = {"Vehicle": "blue", "Cheese": "orange"}

    sns.barplot(
        x="Price",
        y="Item",
        hue="Category",
        data=sorted_df,
        palette=palette,
    )

    plt.title(
        "Price per Pound: Vehicles vs Cheeses (Interleaved, Descending, Max $400)",
        fontsize=16,
    )
    plt.xlabel("Price per Pound (USD)", fontsize=18, labelpad=25)
    plt.ylabel("Items", fontsize=12)
    plt.xscale("log")
    plt.grid(True, which="both", linestyle="--", linewidth=0.5, axis="x")
    plt.xlim(5, 400)
    plt.legend(fontsize=20, title_fontsize=20, bbox_to_anchor=(1.05, 1), loc="upper left")

    ax = plt.gca()
    ax.xaxis.set_major_formatter(FuncFormatter(dollar_formatter))

    dollar_ticks = [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300]
    ax.xaxis.set_ticks(dollar_ticks, minor=True)
    ax.xaxis.set_ticklabels([f"${x}" for x in dollar_ticks], minor=True, fontsize=8)

    plt.tight_layout()
    plt.show()


def main():
    vehicles = {
        "Mitsubishi Mirage": (16695, 2084),
        "Nissan Versa": (16130, 2598),
        "Toyota Corolla": (22050, 2955),
        "Honda Civic": (23950, 2935),
        "Toyota Camry": (28915, 3310),
        "Honda Accord": (29045, 3239),
        "Toyota RAV4": (30025, 3370),
        "Jeep Wrangler": (31895, 4012),
        "Ford Maverick": (25515, 3563),
        "Ford F-150": (39060, 4391),
        "Ram 1500": (41415, 4765),
        "Chevrolet Silverado 1500": (37845, 4410),
        "Tesla Model 3": (40630, 3862),
        "Tesla Model S": (81630, 4560),
        "Rolls-Royce Phantom": (503000, 5644),
        "Mercedes-Benz S-Class": (118450, 4740),
        "BMW 330i": (45495, 3536),
        "Range Rover SE": (109025, 5240),
        "Cadillac Escalade": (86890, 5823),
        "Porsche 911 Carrera": (116050, 3354),
        "Lamborghini Revuelto": (608358, 4188),
        "Ferrari SF90 Stradale": (520000, 3461),
        "Chevrolet Corvette Stingray": (69995, 3366),
        "Ford Mustang GT": (42500, 3832),
        "Lucid Air Pure": (78900, 4564),
        "Nissan Leaf": (29255, 3509),
        "Toyota GR86": (30395, 2811),
        "Rolls-Royce Spectre": (397750, 6537),
        "Ford F-150 Lightning": (49995, 6361),
    }

    cheeses = {
        "Cheddar": 5.62,
        "Mozzarella": 5.58,
        "Swiss": 7.00,
        "Brie": 14.99,
        "Gouda": 11.50,
        "Parmigiano Reggiano": 20.00,
        "Roquefort Blue": 26.00,
        "Goat Cheese": 12.00,
        "Époisses": 30.00,
        "Manchego": 18.50,
        "Gruyère": 22.00,
        "Camembert": 16.75,
        "Stilton": 28.50,
        "Feta": 9.99,
        "Pecorino Romano": 17.25,
        "Burrata": 24.00,
        "Comté": 25.50,
        "Halloumi": 15.75,
        "Taleggio": 19.50,
        "Gorgonzola": 21.00,
        "Emmental": 13.75,
        "Ricotta": 8.50,
        "Mascarpone": 10.25,
        "Provolone": 12.50,
        "Asiago": 16.00,
        "Fontina": 18.75,
        "Havarti": 14.25,
        "Morbier": 23.50,
        "Raclette": 19.75,
        "Mimolette": 27.50,
        "Reblochon": 24.75,
        "Munster": 17.50,
        "Pont-l'Évêque": 29.00,
        "Cabrales": 22.50,
        "Ossau-Iraty": 26.75,
        "Queso Fresco": 7.99,
        "Cotija": 11.25,
        "Paneer": 8.75,
        "Wensleydale": 20.50,
        "Roquefort": 31.00,
    }

    vehicle_prices = get_vehicle_prices_per_kg(vehicles)
    cheeses_prices = get_cheese_prices_per_kg(cheeses)
    plot_price_comparison(vehicle_prices, cheeses_prices)


if __name__ == "__main__":
    main()

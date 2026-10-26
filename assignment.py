
import pandas as pd

filename = "big-mac-full-index.csv"


def get_describe_country(country_code):
    df = pd.read_csv(filename)

    df_country = df[
        df["iso_a3"] == country_code.upper()
    ]

    return df_country["dollar_price"].describe()


def get_country_groupby_year(country_code):
    df = pd.read_csv(filename)

    df_country = df[
        df["iso_a3"] == country_code.upper()
    ].copy()

    df_country["year"] = pd.to_datetime(
        df_country["date"]
    ).dt.year

    return df_country.groupby("year")[
        "dollar_price"
    ].describe()


if __name__ == "__main__":

    countries = ["usa", "mex", "can", "jpn", "gbr"]

    for country in countries:
        print("\nCountry:", country.upper())

        print("\nDescriptive Statistics:")
        print(get_describe_country(country))

        print("\nStatistics by Year:")
        print(get_country_groupby_year(country))

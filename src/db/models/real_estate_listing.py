from pydantic import BaseModel, Field


class RealEstateListing(BaseModel):
    """ A Pydantic model representing a real estate listing. """
    neighborhood: str = Field(description="The neighborhood name of the listing")
    price: str = Field(description="The price of the listing, in USD format: $XXX,XXX")
    bedrooms: int = Field(description="Number of bedrooms in the house (usually 1 to 5)")
    bathrooms: int = Field(description="Number of bathrooms in the house (usually 1 to 3)")
    house_size: str = Field(description="Size of the house in square feet")
    description: str = Field(description="A brief description of the house")
    neighborhood_description: str = Field(description="A brief description of the neighborhood")


class RealEstateListingsResult(BaseModel):
    results: list[RealEstateListing] = Field(description="A list of real estate listings")

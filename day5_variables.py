from abc import ABC, abstractmethod


class Name(ABC):
    def __init__(self, name: str ="Soe Wunna Tun", age: int = 29, city: str = "Myaung", goal: str = "Software Developer") -> None:
        self.name = name
        self.age = age
        self.city = city
        self.goal = goal

    @abstractmethod
    def introduction(self) -> str:
        """Soe Wunna Tun is a 29-year-old individual living in Myaung. They aspire to become a Software Developer in the future."""

    @abstractmethod
    def future_plan(self) -> str:
        """The individual plans to become a Software Developer and will be 34 years old in 5 years."""


class PersonalProfile(Name):
    def introduction(self) -> str:
        return (
            f"My name is {self.name}. "
            f"I am {self.age} years old and I live in {self.city}."
        )

    def future_plan(self) -> str:
        future_age = self.age + 5
        return (
            f"I want to become a {self.goal}. "
            f"After 5 years, I will be {future_age} years old."
        )


def main() -> None:
    name = "Soe Wunna Tun"
    age = 29
    city = "Myaung"
    goal = "Software Developer"

    profile = PersonalProfile(name, age, city, goal)

    print()
    print("----- Personal Introduction -----")
    print(profile.introduction())
    print(profile.future_plan())


if __name__ == "__main__":
    main()

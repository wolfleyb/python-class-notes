#!/usr/bin/env python3

import sys

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

class SmallDog(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)

class LargeDog(Dog):
    def speak(self, sound="Woof"):
        return super().speak(sound)

class JackRussellTerrier(SmallDog):
    pass

class ShiTzu(SmallDog):
    pass

class BullDog(LargeDog):
    pass


teddy = ShiTzu("Teddy", 9)
bo = ShiTzu("Bo",7)
andy = JackRussellTerrier("Andy", 3)
bufurd = BullDog("Bufurd", 12)

dogList = [teddy, bo, andy, bufurd]

dogIter = iter(dogList)

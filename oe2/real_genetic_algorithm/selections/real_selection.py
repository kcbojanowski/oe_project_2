import random
import numpy as np
from real_genetic_algorithm.chromosomes.real_candidates import RealCandidates


class RealSelection:
    def select(self, population: RealCandidates, num_select: int, fitness_function: str, maximization: bool):
        pass


class RealBestSelection(RealSelection):
    def select(self, population: RealCandidates, num_select: int, fitness_function: str, maximization: bool):
        sorted_population = sorted(population, key=lambda individual: individual.calculate_value(),
                                   reverse=maximization)
        return sorted_population[:num_select]


class RealRouletteWheelSelection(RealSelection):
    def select(self, population: RealCandidates, num_select: int, fitness_function: str, maximization: bool):
        fitness_values = [individual.calculate_value() for individual in population]
        if not maximization:
            fitness_values = [1.0 / max(f, 0.00001) for f in fitness_values]
        total_fitness = sum(fitness_values)
        probabilities = [fitness / total_fitness for fitness in fitness_values]
        selected = np.random.choice(population, size=num_select, p=probabilities)
        return selected


class RealTournamentSelection(RealSelection):
    def __init__(self, tournament_size: int):
        self.tournament_size = tournament_size

    def select(self, population: RealCandidates, num_select: int, fitness_function: str, maximization: bool):
        selected = []
        for _ in range(num_select):
            tournament = random.sample(population, self.tournament_size)
            if maximization:
                winner = max(tournament, key=lambda individual: individual.calculate_value())
            else:
                winner = min(tournament, key=lambda individual: individual.calculate_value())
            selected.append(winner)
        return selected

from abc import abstractmethod, ABC

from oe2.generic_algorithm.chromosomes.chromosome import Chromosome


class Crossover(ABC):
    @abstractmethod
    def crossover(self, chromosome1: Chromosome, chromosome2: Chromosome) -> Chromosome:
        if len(chromosome1.binary_representation) != len(chromosome2.binary_representation):
            raise ValueError("N")
        return None
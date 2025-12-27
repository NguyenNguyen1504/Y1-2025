import random


class Protozoan:
    NUMBER_OF_GENES = 10
    GENE_MIN_VALUE = 0
    GENE_MAX_VALUE = 5

    def __init__(self, given_name, genelist):
        self.__name = given_name
        if self.genes_ok(genelist):
            self.__genes = [] + genelist
        else:
            self.__genes = [Protozoan.GENE_MIN_VALUE] * Protozoan.NUMBER_OF_GENES

    def genes_ok(self, list_of_genes):
        if len(list_of_genes) != Protozoan.NUMBER_OF_GENES:
            return False
        for gene in list_of_genes:
            if gene < Protozoan.GENE_MIN_VALUE or \
                    gene > Protozoan.GENE_MAX_VALUE:
                return False
        return True

    def get_name(self):
        return self.__name

    def get_genes(self):
        return self.__genes

    def mutation(self, gene_no, new_gene):
        if 0 <= gene_no < Protozoan.NUMBER_OF_GENES and \
                Protozoan.GENE_MIN_VALUE <= new_gene <= Protozoan.GENE_MAX_VALUE:
            self.__genes[gene_no] = new_gene
            return True
        else:
            return False

    def mate(self, another_protozoan, descendant_name):
        new_genes = [0] * Protozoan.NUMBER_OF_GENES
        for i in range(0, Protozoan.NUMBER_OF_GENES):
            choice = random.randint(1, 3)
            if choice == 1:
                new_genes[i] = self.__genes[i]
            elif choice == 2:
                new_genes[i] = another_protozoan.get_genes()[i]
            else:
                new_genes[i] = (self.__genes[i] + another_protozoan.get_genes()[i]) // 2
        return Protozoan(descendant_name, new_genes)

    def clone(self, clone_name):
        return Protozoan(clone_name, self.__genes)

    def __str__(self):
        return f"Name: {self.__name}, genes: {self.__genes}"
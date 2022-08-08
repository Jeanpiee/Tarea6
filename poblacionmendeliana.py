
import scipy # for random numbers

def build_population(N, p):
    """  Comenzamos construyendo la función de creación de población (en nuestro editor de texto), luego la probamos en la terminal python3.
    The population consists of N individuals """
    population =[]
    for i in range(N):
        allele1 = "A"
        if scipy.random.rand() > p:
            allele1 = "a"
        allele2 = "A"
        if scipy.random.rand() > p:
            allele2 = "a"
        population.append((allele1, allele2))
    return population


# In[3]:


# FUNCIÓN 2. Conteo de pares de alelos
def compute_frequencies(population):
    """ construimos la función 2 que calcula las frecuencias de los genotipos. AA, Aa y aA  son los posibles genotipos. Aa y aA difieren según qué alelo se heredó por vía materna o paterna."""
    AA = population.count(("A", "A"))
    Aa = population.count(("A", "a"))
    aA = population.count(("a", "A"))
    aa = population.count(("a", "a"))
    return({"AA": AA, "aa": aa, "Aa": Aa, "aA": aA})


# In[4]:


# FUNCIÓN 3. Creación de nueva población
def reproduce_population(population):
    """ Esta función 3 acepta la población actual de adultos reproductivos y genera la siguiente generación con el mismo tamaño que la generación anterio:
    - choose the parents at random, 
    - the offspring receives a chromosome from each of the parents.
    """
    new_generation = []
    N = len(population)
    for i in range(N):
        # random integer between 0 and N-1
        dad = scipy.random.randint(N)
        mom = scipy.random.randint(N)
        # which chromosome comes from mom
        chr_mom = scipy.random.randint(2)
        offspring = (population[mom][chr_mom], population[dad][1 - chr_mom])
        #if offspring == ("a", "a"): 
          #next()
        new_generation.append(offspring)
    return new_generation
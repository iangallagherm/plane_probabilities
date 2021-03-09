import argparse

def get_squares_table(prime):
    is_square = [False]*prime
    
    for n in range(prime):
        is_square[(n*n) % prime] = True

    return is_square

def count_planes(prime):
    squares = get_squares_table(prime)

    field_count = 0
    split_count = 0
    nilpotent_count = -1 # Negative 1 offsets the 1 counted for point (0,0,0,0)
                         # which does not generate a nilpotent plane.

    for x in range(prime):
        for y in range(prime):
            for z in range(prime):
                norm = -x*x - y*y + z*z

                if ((norm % prime) == 0):
                    nilpotent_count += 1
                elif (squares[-norm % prime]):
                    split_count += 1
                else:
                    field_count += 1

    # Accounting for multiple counts of the each plane
    field_count //= prime - 1
    split_count //= prime - 1 
    nilpotent_count //= prime - 1

    return [field_count, split_count, nilpotent_count]

def print_plane_probabilities(prime, counts):
    print(f"P = {prime} Plane Counts")
    print(f"Quadratic Extensions: {counts[0]}")
    print(f"Split Planes:         {counts[1]}")
    print(f"Nilpotent Planes:     {counts[2]}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Determines probability of each" +
                                                 " possible quadratic extension" +
                                                 " of a finite field of p elements")
    parser.add_argument("prime", type=int, nargs='+',
                        help='size of the finite field (must be prime)')
    args = parser.parse_args()

    primes = args.prime
    for prime in primes:
        counts = count_planes(prime)
        print_plane_probabilities(prime, counts)

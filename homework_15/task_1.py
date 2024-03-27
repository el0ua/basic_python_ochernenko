class Gogzilla:
    def __init__(self, stomach_valume):
        self.stomach_volume = stomach_valume
        self.current_stomach_volume = 0

    def eat(self, human_valume):
        if self.current_stomach_volume + human_valume <= 0.9 * self.stomach_volume:
            self.current_stomach_volume += human_valume
            print("Godzilla has eaten a human")
        else:
            print("Godzilla is full and can't eat this human.")


def main():
    godzilla = Gogzilla(1000)
    human_volumes = [150, 200, 400, 150, 300]

    for volume in human_volumes:
        godzilla.eat(volume)


if __name__ == "__main__":
    main()
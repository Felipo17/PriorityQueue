import random

class PriorQueue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return str(self.queue)

    def add(self, elem, prio):
        try:
            step = 0
            i = 0
            while prio <= self.queue[i][1]:
                i += 1
                step += 1
            self.queue.append(self.queue[len(self.queue)-1])
            step += 1
            for j in range(len(self.queue), i, -1):
                self.queue[j-1] = self.queue[j-2]
                step += 1
            self.queue[i] = [elem, prio]
            step += 1
        except IndexError:
            self.queue.append([elem, prio])
            step += 1

    def show(self):
        if len(self.queue) == 0:
            print("Queue is empty!")
        else:
            print("(Element, prio)", queue)

    def delete(self):
        if len(self.queue) == 0:
            print("Queue is empty!")
        else:
            self.queue.pop(0)

    def firstel(self):
        if len(self.queue) == 0:
            print("Queue is empty!")
        else:
            print("First element of the queue is:", self.queue[0][0])

    def add_elements(queue, volume):
        elements = []
        for i in range(1, volume+1):
            element = "El_{}".format(i)
            prio = random.randint(1, volume)
            elements.append((element, prio))

        random.shuffle(elements)

        for element, prio in elements:
            queue.add(element, prio)


queue = PriorQueue()

if __name__ == '__main__':

    print("1. Add element to queue")
    print("2. Show queue")
    print("3. Delete element")
    print("4. Display first element of the queue")
    print("5. Create random queue")
    print("6. Exit")

    while True:
        choice = input("Choose function: ")

        if choice == '1':
            elem, prio = input("Note your number then after space note its priority: ").split()
            queue.add(elem, prio)

        if choice == '2':
            queue.show()

        if choice == '3':
            queue.delete()

        if choice == '4':
            queue.firstel()

        if choice == '5':
            queue.add_elements(100)

        if choice == '6':
            break

        if int(choice) not in range(1,7):
            print ("Try again!")

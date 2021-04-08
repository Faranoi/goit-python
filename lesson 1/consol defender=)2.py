from random import randint


def generate_map(x, y, portal_x, portal_y):
     world_map = ''

        for i in range(MAP_SIZE_N):

            row = ''

            for j in range(MAP_SIZE_M):

                cell = '| '

                if x == j and y == i:
                    print(f'Moving character {direction} to {x}:{y}')
                    cell = '|X'
                elif portal_x == j and portal_y == i:
                    cell = '|O'
                    
                row += cell

            row += '|\n'

            world_map += row

        print(world_map)



if __name__ == '__main__':

    MAP_SIZE_N = int(input('Map size n: '))
    MAP_SIZE_M = int(input('Map size m: '))

    x = int(input('Player x: '))
    y = int(input('Player y: '))

    portal_x = randint(0, MAP_SIZE_N - 1)
    portal_y = randint(0, MAP_SIZE_M - 1)

    print(f'Generating map {MAP_SIZE_N}x{MAP_SIZE_M}...')
    direction = 'initially'

    while True:
        generate_map(x, y, portal_x, portal_y)
       
        if x == portal_x and y == portal_y:
            print('You won!')
            break

        action = input('Action: ')

        if action == 'move':
            
            direction = input('Direction: ')

            if direction == 'up' and y > 0:
                y -= 1
            elif direction == 'down' and y < MAP_SIZE_M - 1:
                y += 1
            elif direction == 'left':
                x -= 1
                x = MAP_SIZE_N - 1 if x < 0 else x
            elif direction == 'right':
                x += 1
                x = 0 if x == MAP_SIZE_N else x
            else:
                print('Wrong direction. Please try again.')

        elif action == 'exit':
            break
        else:
            print('Wrong action. Please try again.')

    print('Game Over')

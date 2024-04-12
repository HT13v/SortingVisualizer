import pygame
import time
import random

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Number of elements and their range
NUM_ELEMENTS = 100
MIN_ELEMENT = 10
MAX_ELEMENT = 500
element_width = WIDTH // NUM_ELEMENTS

# Create a list of random elements
elements = [random.randint(MIN_ELEMENT, MAX_ELEMENT) for _ in range(NUM_ELEMENTS)]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Visualizer")

# Main loop
running = True

def draw_elements():
    for i, element in enumerate(elements):
        pygame.draw.rect(screen, BLACK, (i * element_width, HEIGHT - element, element_width, element))

def bubble_sort():
    n = len(elements)
    for i in range(n):
        for j in range(0, n - i - 1):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
                # Redraw the elements after swapping
                screen.fill(WHITE)
                draw_elements()
                pygame.display.update()
                # Add a delay to visualize the sorting process
                time.sleep(0.01)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
        

def run_quick_sort():
    global elements
    elements = quick_sort(elements)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def run_merge_sort():
    global elements
    elements = merge_sort(elements)
import heapq

def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

def run_heap_sort():
    global elements
    elements = heap_sort(elements)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    draw_elements()
    pygame.display.update()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_b]:
        bubble_sort()
    elif keys[pygame.K_q]:
        run_quick_sort()
    elif keys[pygame.K_m]:
        run_merge_sort()
    elif keys[pygame.K_h]:
        run_heap_sort()

pygame.quit()


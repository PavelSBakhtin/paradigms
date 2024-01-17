# Императивное и декларативное программирование на практике. Семинар 01

## Задача №1
Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

## Решение

```python
def sort_list_imperative(numbers):
    for i in range(len(numbers)-1):
        for j in range(len(numbers)-i-1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers
```

---

## Задача №2

Написать точно такую же процедуру, но в декларативном стиле

## Решение

```python
def sort_list_declarative(numbers):
    return sorted(numbers, reverse=True)
```
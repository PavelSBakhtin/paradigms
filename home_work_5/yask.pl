% Rules
sum_list([], 0).
sum_list([H|T], Sum) :-
    sum_list(T, Sum1),
    Sum is H + Sum1.

?- sum_list([1,2,3,4,5,6,7,8,9,10], S),

    write('Суммы элементов списка: '),
    writeln(S),
    write('Список: '),
    write([1,2,3,4,5,6,7,8,9,10]).

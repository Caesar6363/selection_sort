def selection_sort(arr):
    n = len(arr)
    for i in range(n): #создаем итератора i и перебираем список на колличество значений равное длине списка
                        #create iterator i and search the list for a number of values equal to the length of the list
        min_idx = i #передаем_в_новую_переменную_значение_i
                    #transfer_to_new_variable_value_i
        for j in range(i+1, n):  #создаем итератора j и перебираем список на колличество значений в диапазоне от i+1 до n
                                #create iterator j and search the list for the number of values in the range from i+1 to n
            if arr[j] < arr[min_idx]: #выполняем сравнениие, если True то выполняется тело оператора сравнения min_idx = j
                                        #execute_comparison, if True, the body of the comparison operator is executed min_idx = j
                min_idx = j     #передаем_в_новую_переменную_значение_j
                                #transfer_to_new_variable_value_i
        arr[i], arr[min_idx] = arr[min_idx], arr[i] #делаем_обмен_значениями
                                                    #making_the_value_exchange
    return arr

arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print(f"'Сортировка выбором': {sorted_arr}")
def solution(one_day_price, multi_day, multi_day_price, n):
    if one_day_price * multi_day <= multi_day_price:
        return n * one_day_price
    else:
        return (n % multi_day) * multi_day_price + (n // multi_day) * one_day_price
    return 0

if __name__ == "__main__":
    one_day_price, multi_day, multi_day_price, n = 3, 5, 14, 6
    print(f'one_day_price={one_day_price}, multi_day={multi_day}, multi_day_price={multi_day_price}, n={n}, solution should be 17={solution(one_day_price, multi_day, multi_day_price, n)}')

    one_day_price, multi_day, multi_day_price, n = 2, 3, 5, 11
    print(f'one_day_price={one_day_price}, multi_day={multi_day}, multi_day_price={multi_day_price}, n={n}, solution should be 19={solution(one_day_price, multi_day, multi_day_price, n)}')
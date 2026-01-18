def calculate_commission(total_locks, total_stocks, total_barrels):
    LOCK_PRICE = 45.0
    STOCK_PRICE = 30.0
    BARREL_PRICE = 25.0

    LOCK_LIMIT = 70
    STOCK_LIMIT = 80
    BARREL_LIMIT = 90

    if total_locks < 1 or total_stocks < 1 or total_barrels < 1:
        raise ValueError("Must sell at least one lock, stock, and barrel")

    if total_locks > LOCK_LIMIT:
        raise ValueError("Lock limit exceeded")
    if total_stocks > STOCK_LIMIT:
        raise ValueError("Stock limit exceeded")
    if total_barrels > BARREL_LIMIT:
        raise ValueError("Barrel limit exceeded")

    sales = (
        total_locks * LOCK_PRICE +
        total_stocks * STOCK_PRICE +
        total_barrels * BARREL_PRICE
    )

    if sales > 1800:
        return 0.10 * 1000 + 0.15 * 800 + 0.20 * (sales - 1800)
    elif sales > 1000:
        return 0.10 * 1000 + 0.15 * (sales - 1000)
    else:
        return 0.10 * sales
    
def main():
    total_locks = 0
    total_stocks = 0
    total_barrels = 0

    locks = int(input("Locks sold (-1 to finish): "))
    while locks != -1:
        stocks = int(input("Stocks sold: "))
        barrels = int(input("Barrels sold: "))

        total_locks += locks
        total_stocks += stocks
        total_barrels += barrels

        locks = int(input("Locks sold (-1 to finish): "))

    try:
        commission_amount = calculate_commission(
            total_locks, total_stocks, total_barrels
        )
        print(f"Commission is ${commission_amount:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
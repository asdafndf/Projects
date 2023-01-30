# Count the average of arbitary many integer. 
def count_mean(*numbers):
    """
    Counts the average of arbitary many integers
    If no integers are given return 'Invalid input'
    """
    return sum(numbers) / len(numbers) if numbers else "Invalid input"



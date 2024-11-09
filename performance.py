import random

def print_random():
    # 0～1億の範囲でランダムな100万個の数のリストを作成
    random_list = [random.randint(0, 10**8) for _ in range(10**6)]
    
    # 0～1億の範囲でランダムな100個の数を作成
    check_list = [random.randint(0, 10**8) for _ in range(100)]
    
    # random_list を set に変換して、検索の効率を向上
    random_set = set(random_list)
    
    # check_list の各要素が random_set に含まれているか確認
    found_numbers = [num for num in check_list if num in random_set]
    
    if found_numbers:
        print(f"Found {len(found_numbers)} numbers: {found_numbers}")
    else:
        print("No matching numbers found.")

# このファイルが直接実行されたときにのみ print_random を実行
if __name__ == '__main__':
    print_random()

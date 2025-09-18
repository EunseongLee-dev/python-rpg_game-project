# Python RPG Project – Inventory/Item 구현 시도 (Markdown 기록 예시)

## 날짜
2025-09-18

## 진행한 내용
- `Item` 클래스 구현:
  - 속성: `name`, `type`, `value`
  - 메서드: `Gold`, `drop_item` 기본 구조 작성
- `Inventory` 클래스 구현:
  - 속성: `items` (리스트)
  - 메서드: `add_item`, `remove_item`, `show_inventory`

## 구현 코드 (현재까지)
```python
from random import *

Item_list = {
    "Sword": {"type": "equipment", "value": 2},
    "Small Gold Pouch": {"type": "gold-item", "value": 50},
    "Leather Boots": {"type": "equipment", "value": 1}
}

class Item():
    def __init__(self, name, type, value):
        self.name = name
        self.type = type
        self.value = value

    def Gold(self, amount: int):
        return randint(10, 100)

    def drop_item(self):
        choice(list(Item_list.keys()))

class Inventory():
    def __init__(self, items: list[Item]):
        self.items = items

    def add_item(self, item: Item):
        self.items.append(item)

    def remove_item(self, name: str):
        if name in self.items:
            self.items.remove(name)
            print(f"{name} 아이템을 버렸습니다.")
            return True
        else:
            print(f"{name} 아이템을 찾지 못했습니다.")
            return False

    def show_inventory(self):
        for i in self.items:
            print(f"{i.name}: {i.type} / {i.value}")
```

## 고민, 막혔던 점, 의문
- `Gold` 메서드에서 amount 매개변수는 외부에서 받아야 하는지, 내부에서 랜덤 결정되는지 혼란
- `drop_item` 메서드에서 `Item_list`에서 랜덤으로 아이템 선택 후 실제 `Item` 객체로 변환하는 흐름이 불분명
- `Inventory` 클래스에서 `items: list[Item]` 형태가 정확히 무슨 의미인지 이해가 어려움
- 리스트에 `Item` 인스턴스를 넣으면 자동으로 `Item(...)`처럼 보이는 원리 이해 부족
- `add_item`에서 `item: Item`이라고 적은 것의 의미(클래스 참조) 혼동
- 상속과 참조의 차이, Item 클래스 상속 없이 참조만으로도 충분한지 의문
- 전체적으로 구현 시도는 했지만 로직 연결과 실행까지 이어지는 흐름이 막연함

## 다음 시도 계획
1. `drop_item`에서 실제 `Item` 객체를 반환하도록 구현
2. 플레이어 객체에 연결해 `add_item`으로 인벤토리에 누적
3. `Gold` 획득 로직과 실제 플레이어 `gold` 속성과 연결
4. `show_inventory` 출력 테스트 및 리스트 내 Item 객체 구조 확인
5. 각 기능 별 출력 순서와 연결 구조 고민

## 느낀 점
- 단순히 메서드 하나 작성하는 것도 여러 부분에서 참조, 랜덤, 리스트 조합 등 생각해야 할 점이 많아 막막함
- 오늘은 스킬 구현보다 더 막연하고 난이도 높은 도전이었음
- 구현과 연결 흐름, 속성 활용을 동시에 고려하는 연습 필요
- 막혔던 부분, 의문점 기록이 향후 문제 해결과 코드 정리 시 큰 도움이 될 것이라 판단


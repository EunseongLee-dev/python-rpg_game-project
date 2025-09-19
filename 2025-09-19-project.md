# 오늘 프로젝트 정리

## 1. 오늘 구현한 부분

### 아이템 드랍 및 골드 획득
- `item.py`에서 `Item` 클래스와 `drop_item`, `drop_gold` 메서드 구현
- 몬스터 사망 시 배틀에서 아이템과 골드 드랍이 정상 작동
- 아이템 인스턴스 생성 후 플레이어 인벤토리에 추가
- `gold-item`은 add_gold를 통해 플레이어 골드 증가

### 배틀 턴 처리 (fight_turn)
- 플레이어 스킬과 몬스터 스킬 각각 사용 가능하도록 수정
- 플레이어와 몬스터 체력 확인 후 몬스터 사망 시 아이템/골드 드랍 처리
- `player_action`과 `player_skill`, `monster_skill`을 파라미터로 받아 처리하도록 변경

### 인벤토리 구현
- `Inventory` 클래스 생성 (items 리스트 관리)
- `add_item`, `remove_item`, `show_inventory` 메서드 구현
- 플레이어 클래스에서 `self.inventory = Inventory([])`로 연동

### 출력 확인
- 골드 및 아이템 획득 출력 정상 작동
- `Inventory.show_inventory()` 메서드로 아이템 확인 가능

## 2. 햇갈리거나 잘못됐던 부분

### drop_item / drop_gold 연결
- 초기에는 battle에서 직접 drop_gold를 호출했음
- item.py에 drop_gold, drop_item이 있으므로 몬스터 클래스에서 이를 호출해야 함
- battle에서 self.monster.drop_item()만 사용하면 몬스터가 가진 메서드가 아니므로 에러 발생

### 인벤토리와 Item 클래스
- Item 클래스에 `__str__` 정의했지만 `inventory.items` 리스트를 그대로 출력하면 `<Item object>`로 나옴
- show_inventory 메서드를 사용해야 인벤토리 내용을 보기 좋게 출력 가능
- 마지막에 None 출력은 print(show_inventory()) 형태로 호출했기 때문

### fight_turn에서 스킬 처리
- 이전에는 몬스터가 플레이어 스킬을 사용함 (잘못된 참조)
- 파라미터로 `player_skill`, `monster_skill`을 받아 각각 사용할 수 있도록 수정
- 한 번 호출로 동시에 플레이어와 몬스터 스킬 처리 가능

### 체력 초기화 문제
- 배틀 종료 후 재배틀 시 체력/상태가 누적됨
- 배틀 시작 전 체력 초기화 필요 (수동, Battle 클래스 메서드, 혹은 fight_turn 내 자동 초기화)

### 기타
- return의 의미와 위치에 대한 이해 필요
  - 함수 내에서 값을 외부로 전달할 때 사용
  - 특정 조건에서 함수 종료 용도로도 사용 가능 (`if x is None: return`)
- self.inventory = Inventory([])에서 []는 인벤토리 리스트 초기화를 위해 필요
- 골드 누적 확인 시 battle 진행 후 print로 확인해야 함, battle 호출하지 않으면 값 0으로 나옴



- mom과 dad가 집에 도착 ( two process )

- 냉장고 확인 ( check )

- 우유가 비었다면, 우유를 사서 냉장고에 저장 ( file write )
- 우유가 채워져 있다면 pass 

- Race condition 발생 case 
( 두 process가 모두 냉장고에 접근하여 우유가 없는것을 확인하고 우유를 사고 저장하는 경우 발생)


-----------------------
해결 ( semaphore )

누군가 냉장고에 접근하고 우유를 빈것을 확인 ( check )
우유를 사서 냉장고에 저장 ( working)

위 작업을 진행하는 동안 다른 process는 냉장고에 접근을 막는다. (semaphore)

key를 가진 사람이 key를 get하고(get) 냉장고를 확인하고(check), 우유를 저장하고(modify) key를 반납한다.(release)

다른 누군가는 key를 get할 수 없다면 key를 get할 때까지 대기한다 (wait)


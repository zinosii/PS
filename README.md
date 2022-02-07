# PS
* 2022.02.04  
  + <boj 9328, 열쇠>
    * 처음 풀이 :<br> **1**. 가장자리에 위치한 빈공간을 모두찾은후, 빈 공간의 좌표를 담는 큐를 만듬.<br> **2**. 그 큐가 빌때까지 bfs. 만약 한 위치에서 탐색하며 문을 만난경우, 그 문을 열 수 없으면 다시 큐에 넣어주어야함(나중에 열쇠를 얻을수 있으므로) 여기서 시간이 많이쓰임 
    * 더 나은 풀이 :<br> **1**. h,w 입력받고, 지도를 감싸는 빈공간을 생성해줌, 즉 지도의 사이즈를 (h+2) * (w+2)로 변경.<br> **2**. door queue 를 만들어서 그에 해당하는 key를 얻으면, 그 문의 위치를 다시 position queue 로 넘겨주어 (0,0)에서 시작하는 bfs한번만에 풀이가능
+ 2022.02.05 
  + <boj 9466, 텀프로젝트> 
    + 처음 풀이 :<br> **1**. 각 학생이 선택한 학생의 정보를 담는 Choice 리스트와, 각 학생의 상태를 담는 visit리스트를 만듬 visit이 -1 일경우 방문을 안한 경우, 0일 경우 팀을 못 이룬 경우, 1일 경우 팀을 이룬것.<br> **2**. 1부터 N번 까지, visit이 -1인 경우만 함수실행.<br> **3**. 함수의 인자는 학생의 번호, 지금까지 선택된 학생의 정보를 담는 리스트와 집합이있는데, 각 함수마다 학생이 선택한 학생이 팀원리스트에 있는지 확인하기 위해 set을 같이 사용함 **-> 시간복잡도를 줄여 AC를 받을수있었음.**<br> **4**. 만약 선택한 학생이 집합내에 있을경우, 리스트의 순서대로 팀을 이뤘는지 판단가능 하므로 visit 업데이트. 
    + 더 나은 풀이 :<br> **1**. 방문한 학생들의 번호를 담는 집합 team 을 만듬.<br> **2**. 각 학생마다 dfs시작, dfs시작시 바로 방문처리를 해줌.<br> **3**. 만약 선택한 학생이 방문 처리된 경우, cycle을 이루는지 확인하여 cnt를 증가시켜줌. dfs마지막에는 team집합 업데이트.
  + <boj12852, 1로 만들기 2>
    + 이 문제는 bfs와 dp 두가지로 풀수있었음.
    + dfs풀이 :<br> **1**. N을 입력받고 N으로부터 bfs시작. bfs는 숫자와 지금까지 방문한 숫자 리스트의 정보가 담김.<br> **2**. visit리스트를 만들어 방문된경우 bfs큐 에 넣어줄 필요없음. 1이 되면 종료
    + DP풀이 :<br> **1**. DP리스트와 정답의 정보를 담을 ans리스트를 만듬. DP는 최댓값으로 채워주고, DP[1]=0으로 초기화 함으로써 DP를 1부터 채워줌.<br> **2**. ans배열은 이값을 만들수있는 숫자의 정보를 담음 ex) ans[10]은 9에서 오거나 5에서 올수있음. 둘중 더 작은 DP를 갖는 9로 부터 10이 채워짐.<br> **3**. DP[N]을 출력하고 N, ans[N]에서 ans[1]로 갈때까지 while문 으로 출력해줌.
  + <boj10775, 공항>
    + 처음 풀이 :<br> **1**. 시간복잡도가 O(N^2)로 TLE가 나옴 Greedy 하게 주어진 게이트 부터 작은 게이트 번호로 가면서 모든 게이트를 방문하였으면 답을 출력 하도록 코드를 짰더니, 도킹 가능한 게이트를 찾는과정에서 시간소비가 너무 컸음. -> 개선해야함<br> **2**. 새로운 리스트 A를 만듬. A[i]는 i번째 게이트가 입력되었을때, 그 게이트 번호부터 도킹 가능한 게이트를 의미함. 즉 처음 초기화시 [1,2,3,4,...,G]의 형태임.<br> **3**. 이전 풀이와 차이점은 게이트 번호 g를 A[g]로 바꿔주는 것과 A리스트를 업데이트하는데 있음. 만약 k번 게이트를 통해 도킹에 성공 하였다면, A[k]의 값을 1줄여야함. 그 외는 이전 풀이와 동일.
+ 2022.02.06 **[solved.ac P5달성!]**
  + <boj 10942, 팰린드롬?>
    + 처음풀이 :<br> **1**. DP로 풀었음. DP[s][e]의 의미는 s~e가 팰린드롬이면 1, 아니면 0을 저장함. s와 e가 같으면 1, s+1==e 면 두 문자가 같은지 비교. 그외에는 s와 e만을 비교하여 판단 할 수 있음.<br> **2**. 만약 s와 e가 다르다면, 무조건 팰린드롬이 될수없고, 같다면 s+1과 e-1을 비교 해보면 됨.
    + 더 나은 풀이 :<br> **1**. 이 문제를 통해서 새로운 알고리즘을 알게되었는데, 팰린드롬을 더 빠르게 구하기 위한 manacher 알고리즘임.<br> **2**. manacher 알고리즘의 시간복잡도는 O(n)으로 매우 빠른데, 핵심아이디어는 팰린드롬의 중심점으로 부터 대칭되는 부분 문자열 역시 팰린드롬이 된다는 것에서 시작함.<br> **3**. 부분 문자열의 길이가 짝수일경우 구할수 없는 알고리즘이기 때문에 부분 문자열의 길이가 짝수일때를 구해주기 위해 문자열 중간에 특수문자를 삽입해야함. 즉 banana->b#a#n#a#n#a.
+ 2022.02.07
  + <boj 1202, 보석도둑>
    + 복습 :<br> **1**. 우선순위 큐를 두번 사용하여 푸는문제, 처음 풀때는 어떻게 접근해야 할지 몰랐음. 보석pq와 보석의 가치를 담는 pq를 이용하면 쉽게 풀 수 있음. 가방무게에 맞게 가장 높은 가치의 보석을 정답에 더해주면 된다는것을 인지하고 가방 리스트가 빌때까지 반복해주면 됨.

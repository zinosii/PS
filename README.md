# PS
<details><summary> 2022.02 </summary><blockquote>
<details><summary> 2022.02.04 </summary><blockquote>
<details><summary> boj 9328, 열쇠 </summary>
  
+ 처음 풀이 :<br> **1**. 가장자리에 위치한 빈공간을 모두찾은후, 빈 공간의 좌표를 담는 큐를 만듬.<br> **2**. 그 큐가 빌때까지 bfs. 만약 한 위치에서 탐색하며 문을 만난경우, 그 문을 열 수 없으면 다시 큐에 넣어주어야함(나중에 열쇠를 얻을수 있으므로) 여기서 시간이 많이쓰임 
+ 더 나은 풀이 :<br> **1**. h,w 입력받고, 지도를 감싸는 빈공간을 생성해줌, 즉 지도의 사이즈를 (h+2) * (w+2)로 변경.<br> **2**. door queue 를 만들어서 그에 해당하는 key를 얻으면, 그 문의 위치를 다시 position queue 로 넘겨주어 (0,0)에서 시작하는 bfs한번만에 풀이가능
</details>
</blockquote></details> 
<details><summary> 2022.02.05 </summary><blockquote>
<details><summary> boj 9466, 텀프로젝트 </summary>
  
+ 처음 풀이 :<br> **1**. 각 학생이 선택한 학생의 정보를 담는 Choice 리스트와, 각 학생의 상태를 담는 visit리스트를 만듬 visit이 -1 일경우 방문을 안한 경우, 0일 경우 팀을 못 이룬 경우, 1일 경우 팀을 이룬것.<br> **2**. 1부터 N번 까지, visit이 -1인 경우만 함수실행.<br> **3**. 함수의 인자는 학생의 번호, 지금까지 선택된 학생의 정보를 담는 리스트와 집합이있는데, 각 함수마다 학생이 선택한 학생이 팀원리스트에 있는지 확인하기 위해 set을 같이 사용함 **-> 시간복잡도를 줄여 AC를 받을수있었음.**<br> **4**. 만약 선택한 학생이 집합내에 있을경우, 리스트의 순서대로 팀을 이뤘는지 판단가능 하므로 visit 업데이트. 
+ 더 나은 풀이 :<br> **1**. 방문한 학생들의 번호를 담는 집합 team 을 만듬.<br> **2**. 각 학생마다 dfs시작, dfs시작시 바로 방문처리를 해줌.<br> **3**. 만약 선택한 학생이 방문 처리된 경우, cycle을 이루는지 확인하여 cnt를 증가시켜줌. dfs마지막에는 team집합 업데이트.
</details>
<details><summary> boj12852, 1로 만들기 </summary>
  
+ 이 문제는 bfs와 dp 두가지로 풀수있었음.
+ dfs풀이 :<br> **1**. N을 입력받고 N으로부터 bfs시작. bfs는 숫자와 지금까지 방문한 숫자 리스트의 정보가 담김.<br> **2**. visit리스트를 만들어 방문된경우 bfs큐 에 넣어줄 필요없음. 1이 되면 종료
+ DP풀이 :<br> **1**. DP리스트와 정답의 정보를 담을 ans리스트를 만듬. DP는 최댓값으로 채워주고, DP[1]=0으로 초기화 함으로써 DP를 1부터 채워줌.<br> **2**. ans배열은 이값을 만들수있는 숫자의 정보를 담음 ex) ans[10]은 9에서 오거나 5에서 올수있음. 둘중 더 작은 DP를 갖는 9로 부터 10이 채워짐.<br> **3**. DP[N]을 출력하고 N, ans[N]에서 ans[1]로 갈때까지 while문 으로 출력해줌.
</details>
<details><summary> boj10775, 공항 </summary>
  
+ 처음 풀이 :<br> **1**. 시간복잡도가 O(N^2)로 TLE가 나옴 Greedy 하게 주어진 게이트 부터 작은 게이트 번호로 가면서 모든 게이트를 방문하였으면 답을 출력 하도록 코드를 짰더니, 도킹 가능한 게이트를 찾는과정에서 시간소비가 너무 컸음. -> 개선해야함<br> **2**. 새로운 리스트 A를 만듬. A[i]는 i번째 게이트가 입력되었을때, 그 게이트 번호부터 도킹 가능한 게이트를 의미함. 즉 처음 초기화시 [1,2,3,4,...,G]의 형태임.<br> **3**. 이전 풀이와 차이점은 게이트 번호 g를 A[g]로 바꿔주는 것과 A리스트를 업데이트하는데 있음. 만약 k번 게이트를 통해 도킹에 성공 하였다면, A[k]의 값을 1줄여야함. 그 외는 이전 풀이와 동일.
</details>
</blockquote></details> 
<details><summary> 2022.02.06 </summary><blockquote>
<details><summary> boj 10942, 팰린드롬? </summary>
  
+ 처음풀이 :<br> **1**. DP로 풀었음 . DP[s][e]의 의미는 s~e가 팰린드롬이면 1, 아니면 0을 저장함. s와 e가 같으면 1, s+1==e 면 두 문자가 같은지 비교. 그외에는 s와 e만을 비교하여 판단 할 수 있음.<br> **2**. 만약 s와 e가 다르다면, 무조건 팰린드롬이 될수없고, 같다면 s+1과 e-1을 비교 해보면 됨.
+ 더 나은 풀이 :<br> **1**. 이 문제를 통해서 새로운 알고리즘을 알게되었는데, 팰린드롬을 더 빠르게 구하기 위한 manacher 알고리즘임.<br> **2**. manacher 알고리즘의 시간복잡도는 O(n)으로 매우 빠른데, 핵심아이디어는 팰린드롬의 중심점으로 부터 대칭되는 부분 문자열 역시 팰린드롬이 된다는 것에서 시작함.<br> **3**. 부분 문자열의 길이가 짝수일경우 구할수 없는 알고리즘이기 때문에 부분 문자열의 길이가 짝수일때를 구해주기 위해 문자열 중간에 특수문자를 삽입해야함. 즉 banana->b#a#n#a#n#a.
+ 솔브닥 P5달성!
</details>
</blockquote></details> 
<details><summary> 2022.02.07 </summary><blockquote>
<details><summary> boj 1202, 보석도둑 </summary>
  
+ 복습 :<br> **1**. 우선순위 큐를 두번 사용하여 푸는문제, 처음 풀때는 어떻게 접근해야 할지 몰랐음. 보석pq와 보석의 가치를 담는 pq를 이용하면 쉽게 풀 수 있음. 가방무게에 맞게 가장 높은 가치의 보석을 정답에 더해주면 된다는것을 인지하고 가방 리스트가 빌때까지 반복해주면 됨.
</details>
<details><summary> boj 12100, 2048(Easy) </summary>
  
+ 처음 풀이 :<br> **1**. 구현+백트래킹 문제. 일단 초기 조건을 Board에 입력받고, 왼쪽으로의 이동만 구현후 rotate함수를 이용해 모든 경우 4^5개를 탐색함.<br> **2**. 최댓값을 구할땐 왼쪽으로 옮기는 경우 숫자가 합쳐질때만 계산하였는데, 그 숫자가 현재의 최댓값인 ans보다 큰지 판단하여 ans를 업데이트 해줌. 답인 ans출력.
</details>
</blockquote></details> 
<details><summary> 2022.02.08 </summary><blockquote>
<details><summary> boj 15956, 숏코딩 </summary>
  
+ 어렵다. 아직못품...
</details>
</blockquote></details>
<details><summary> 2022.02.09 </summary><blockquote>
<details><summary> boj 15956, 숏코딩 </summary>
  
+ 드디어 풀었다... 진짜 너무 어려웠음. 내가 떠올린 방법은 길이를 따로 입력받아 가장 작은 길이로 Union 하는것이였는데, 시간이 너무 오래 걸렸음.<br> 애초에 이럴 필요없이 ==인 양쪽 단항식은 작은 index로 union 해주고 나중에 길이를 판단하여 시간을 줄일 수 있었음.<br> 또한 answer스택에 각각 정답의 요소들을 입력받아 나중에 스택이 빌때까지 pop하며 한번에 출력하는 식으로 출력방법도 수정하였음. 또한 숫자를 굳이 문자열에서 정수형으로 변환하지 않아도 됐었음.<br> ==,!= 에 따라 양쪽 단항식을 지금까지 나온 모든 단항식을 담는 Compoenents 리스트에 담아주며 Union-Find 를 위한 Parents리스트도 업데이트 해준후, ==의 양쪽을 Union하기 위해 left의 부모indx와 right의 부모index의 정보를 한번에 입력받는 새로운 리스트를 만들어(!=도 마찬가지로 만들어줌) Union을 해준후, 최종적으로 dictionary에 index:[...] 꼴로 같은 문자열끼리 묶어줌.<br> 그 후 정수가 두개 이상 있으면 안되므로 이경우도 체크해주고, 각각 길이를 비교하며 가장작은 길이의 문자열을 0번 인덱스와 swap해줌.<br> 그 후 answer에 각 index마다의 답을 넣어주어 ==을 처리하고, !=에서의 답을 추출해야함.<br> !=에서 중복을 해결하기 위해 set자료형으로 !=에 해당하는 답을 받아야함. 작은 인덱스를 앞에두고, 둘의 부모를 찾아 부모가 같은경우 모순이므로 exit(0)을 해주고, 두개가 모두 숫자일경우 continue를 해줌. 이후 두 인덱스의 가장작은 문자열은 가장 앞에있는 값으로 바꿔주었으므로, 0번 값을 넣어줌.<br> 마지막으로 만약 answer가 비어있으면 무조건 True이므로 이경우에도 exit을 해줌.<br> **나중에 무조건 다시풀자**
</details>
</blockquote></details>  
<details><summary> 2022.02.10 </summary><blockquote>
<details><summary> boj 16946, 벽 부수고 이동하기 4 </summary>

+ 보자마자 여러 풀이가 생각이 났지만, 처음 답안을 제출했을땐 역시나 TLE를 받았다.<br> 처음 제출한 코드는 모든 점에 대해서 bfs를 호출하므로 역시나 시간초과였고, 두번째 풀이는 0으로만 이루어진 구역을 나누어 각각구역의 값만큼을 bfs로 구하여 저장한후, 0인점에서 인접한 방향만 계산 해주는 방식으로 구하였다.<br> 그러나 역시 이방법도 TLE가 났는데, 출력 부분을 join으로 해주니 AC를 받을 수 있었다.<br> join을 애용하자...  
</details>
<details><summary> boj 16566, 카드 게임 </summary>
  
+ 이분탐색과 유니온파인드 문제. 처음 생각했을땐 리스트에서 사용한 숫자를 빼주는 방법을 생각해서 이러면 무조건 TLE가 나올 것 이라 생각하여, 다른 방법을 생각해봤는데 그 방법이 Union-Find 였는데 바로 AC를 받았다.<br> 개인적으로 문제티어(P5)에 비해 매우 쉽게 푼 문제였다. 처음 풀이에서 카드숫자가 중복이 허용되니 UpperBound 값을 저장하는 리스트를 만들어 같은 숫자가 나오면 리스트에 바로 접근하여 return 하게 하였는데, 애초에 UpperBound 함수가 매우 빨라 시간이 더 소요가 됐다.
</details>
</blockquote></details>
<details><summary> 2022.02.11 </summary><blockquote>
<details><summary> boj 20040, 사이클 게임 </summary>

+ 무난한 union find 문제. union find 연습용으로 괜찮은 난이도의 문제였다.<br> (+)시간소모를 최대한 줄였더니 처음으로 백준 python제출 에서 가장 위에 내아이디가 떠있었다ㅎ
</details>
</blockquote></details>
<details><summary> 2022.02.12 </summary><blockquote>
<details><summary> boj 15907, Acka의 리듬 세상 </summary>

+ 처음 풀이 :<br> **1**. 에라토스테네스의 체로 m이하 모든 소수를 구하여, 모든 소수에 대하여 각각의 나머지가 같은것의 최댓값을 구해주었는데, 이러면 O(nm)이라 시간초과가 나올 수 밖에 없었다.<br> **2**. lower bound를 이용해 특정 소수 미만의 값은 값을 1로 두고 소수이상의 값만 나머지 계산을 해주었더니 AC를 받을 수 있었다.
+ 더 나은 풀이(최적화) :<br> **1**. 모든 소수에 대해 탐색해도 AC를 받았으나, 비둘기집의 원리를 이용한 최적화 방법이 있었다.<br> **2**. 만약 소수가 2였다면, 홀수아니면 짝수의 갯수가 정답이 되므로 모든 소수에 대하여 정답의 하한은 N/2가 될 수 밖에 없다. 그러므로 소수 k에 대하여 답이 a가 되려면, `k*a`가 m보다는 무조건 작거나 같아야 하므로 `k*N/2`가 무조건 m이하 여야한다.<br> **3**. 그러므로 k를 2*m/n 까지만 탐색해주면 된다.
</details>
<details><summary> boj 6549, 히스토그램에서 가장 큰 직사각형 </summary>

+ 고민을 많이해봤는데, 솔루션을 보니 생각보다 더 어려운 문제였다
+ 처음 풀이 :<br> **1**. 모든 높이에 대해 그 높이보다 큰 값이 연속적으로 나오는 횟수의 최댓값을 구하여 `h*w` 로 구현하였더니, O(n^2*T)로 시간초과를 받았다.
+ 더 나은 풀이 1(스택) :<br> **1**. 스택을 선언하고, 높이를 push해주는데 이때 스택의 top보다 작다면, while문을 이용해 작거나 같은값이 나올때까지 스택에 pop을 해주며 넓이의 값을구하며 최댓값을 갱신해준다.<br> **2**. 위 과정이 끝나고 스택에 비어있지 않다면, w를 N[0]로 선언하여 각각 높이에 대해 넓이를 다시 갱신해준다. 
+ 더 나은 풀이 2(분할정복 & seg tree) :<br> **1**. 이 풀이의 아이디어는 분할정복에서 시작되는데, 기준점을 잡고 그 기준점을 기준으로 왼쪽영영과 오른쪽영역, 그리고 자기 자신의 높이로 만들수있는 총 3개의 영역의 넓이를 비교하는 것이다.<br> **2**. 여기서 만약 기준점을 구간의 최솟값(높이의 최솟값)으로 잡는다면, 기준점의 높이가 최소의 높이이므로 자신을 포함한 영역의 최댓값은 h*(구간의 길이) 가 될것이다. 구간의 최솟값을 구하기 위해  segment tree를 사용한다.<br> **3**. 구간의 최솟값을 구하기위해 segment tree를 사용하는 점이 중요했던것 같다. 
</details>  
</blockquote></details>
<details><summary> 2022.02.13 </summary><blockquote>
<details><summary> boj 12850, 본대 산책2 </summary>
  
+ 처음 풀이 :<br> **1**. 처음에 행렬곱을 떠올리지 못해서 고민하다가, 행렬곱을 떠올리고 바로 풀 수 있었다. 추가로, N%2==1 임을 확인할때 N&1로 비트 연산을 사용하는 습관을 들여야겠다.
</details>
</blockquote></details>
<details><summary> 2022.02.14 </summary><blockquote>
<details><summary> boj 13460, 구슬 탈출 2 </summary>

+ 매우 빡센 구현 문제. 디버깅할때 놓친부분이 없는지 꼼꼼히 체크하자.  
</details>
<details><summary> boj 3109, 빵집 </summary>

+ 처음봤을때는 고민을 좀 했으나 직접 시뮬레이션해보니 그리디로 풀면 풀릴것같아서 바로 풀었음.<br> 처음엔 자꾸 TLE가 나와서 고민해봤는데 방문체크를 굳이 역추적해줄 필요가 없었음. 참신했던 그리디 문제.
</details>
</blockquote></details>
<details><summary> 2022.02.15 </summary><blockquote>
<details><summary> boj 14939, 불 끄기 </summary>
  
+ 개인적으로 풀이가 매우 신기했었음
+ 접근 :<br> **1**. 우선순위큐에 켜진스위치를 상하좌우 그리고 자신까지 5방향에 대해 조사하여 넣어주며 전체 Board를 업데이트하는 방식으로 접근하였으나, 예상했던대로 WA였으며, 도저히 풀이가 떠올리지 않아 해답을 참고하였음. 
+ 해답 :<br> **1**. 생각보다 구현은 쉬웠으나, 이런 아이디어를 떠올린다는게 매우 신기했었음.<br> **2**. 일단 주요 아이디어는 윗방향의 불이 켜져있는지의 여부를 확인하여 총10*10번만 확인하면 되는것인데, 여기서 중요한점이 가장윗줄은 윗방향의 불이 없으므로 2^10=1024번의 불을 키는 모든경우의 백트래킹이 필요했음. 그리고 마지막줄이 모두 꺼지지않았다면, 실패한 케이스로 처리함. 또한 리스트를 복사할때 copy를 쓰면 시간이 더 걸린다는 것을 알았음.<br> **3**. 풀이 보고 바로 이해하였으나, 이러한 풀이를 생각해낼수 있도록 더욱 열심히 해야겠다.
</details>
</blockquote></details> 
<details><summary> 2022.02.16 </summary><blockquote>
<details><summary> boj 16724, 피리 부는 사나이 </summary>
  
+ 처음풀이 :<br> **1**. 간단한 Union-Find 문제인줄 알았으나, 한번 WA를 받았음.<br> **2**. 틀린이유를 찾아보니, 마지막에 전체적으로 Parent리스트를 갱신해주어야 했었음.
</details>
<details><summary> boj 1006, 습격자 초라기 </summary>

+ 사실 한달전에 유명한 문제라 접해봤었는데, 한달지나고 봐도 여전히 어려웠다.. DP문제들은 역시 여러유형을 풀어보고 몸에 체화시켜야겠다.
+ 해답 :<br> **1**. 가장먼저 원형임을 인지하고 풀어야하는데, 이경우를 총 4가지로 나눠 줄 수 있었다. 1번경우는 안쪽과 바깥쪽모두 맨끝과 연결하지 않는 경우, 2번은 안쪽만 연결하는 경우, 3번은 바깥쪽만 연결하는 경우, 4번은 모두 연결되는 경우이다. 각각의 경우에서 ans를 구해주면 되는문제.<br> **2**. 그 후 DP를 채워야하는데, 총 3개의 DP테이블을 만들고 하나는 안쪽의 정보를 담당하고, 다른 하나는 바깥쪽, 마지막 하나는 안쪽,바깥쪽 모두 고려해서 DP를 채워나간후 각각케이스에 맞게 DP의 최종값을 ans와 비교하여 ans를 업데이트 하면 된다.<br> **3**. 나중에 이글을 읽고 다시 풀 수 있을지 의문이지만 꼭 다시 풀어봐야할 DP문제였다.
</details> 
</blockquote></details>   
<details><summary> 2022.02.17 </summary><blockquote>
<details><summary> boj 1014, 컨닝 </summary>
  
+ 한번 WA를 받고 반례를 알고도 도저히 모르겠어서 해답을 참고했는데, 여러풀이가 가능했고 bitmask+DP로 해결하였다.
+ 해답 :<br> **1**. 먼저 DFS를 통해 각 줄마다 가능한 배치를 찾아줘야한다. 이경우 C=3 이라면 ['000', '001', '010', '100', '101'] 이 가능하다.<br> **2**. 그 후 DP를 채워야하는데, 이 때 이전배치의 비트마스크를 이용해야한다. 그러므로 DP를 DP=[[-1]*(1<<C) for _ in range(R)] 형식으로 만들어줘야한다.<br> **3**. 이후 dp함수를 통해 값을 채워 줄 수 있다. cnt를 통해 최대로 앉을수있는 사람수를 계산하고 비트 값을 갱신해주면서 ans를 갱신해주고 최종적으로 DP[0][0]이 답이 된다.
+ 사실 잘 이해가 안되는 문제.. 다시 풀어보자.
</details> 
</blockquote></details> 
<details><summary> 2022.02.18 </summary><blockquote>
<details><summary> boj 1004, 어린 왕자 </summary>
  
+ 원의 정의를 이용하여 푸는 간단한 수학 문제. 쉽게 풀어냈다.
</details> 
<details><summary> boj 1655, 가운데를 말해요 </summary>
  
+ 처음 봤을때 우선순위 큐를 이용해야겠다는 생각까지는 했지만.. 어떤식으로 써야할지 감이안잡혀 못풀었던 문제다.
+ 해답 :<br> **1**. minheap 과 maxheap을 만들고, 가장 핵심이 되는 부분은 최대힙의 원소갯수가 항상 최소힙의 원소갯수보다 1크거나 같아야 한다는점임.<br> **2**. 중간값을 추출해야하므로, 모든 minheap의 원소들은 maxheap의 모든 원소보다 항상 크게 만들어 주기만 하면, maxheap의 top값이 반드시 중간값이 됨.<br> **3**. 이 때 두힙의 원소갯수가 같은경우가 총원소갯수가 짝수인경우인데, 이경우또한 maxheap의 top이 minheap의 top보다 작아야하므로 답이 됨.
</details> 
</blockquote></details> 
<details><summary> 2022.02.19 </summary><blockquote>
<details><summary> boj 2812, 크게 만들기 </summary>
  
+ 구간의 가장 큰 값을 저장하는 segment tree를 이용하여 간단하게 풀 수 있었다. 이외에도 여러 풀이가 있었는데, 그 중스택을 이용한 풀이가 매우 참신하였음.
</details> 
</blockquote></details>  
<details><summary> 2022.02.20 </summary><blockquote>
<details><summary> boj 2042, 구간 합 구하기 </summary>
  
+ segment tree를 이용하여 구간의 합을 빠르게 구할 수 있었음. segment tree 자료구조를 잘 이용하자.
</details> 
</blockquote></details> 
<details><summary> 2022.02.21 </summary><blockquote>
<details><summary> boj 1019, 책 페이지 </summary>
  
+ 수학문제여서 금방 풀 줄 알았으나 못 풀었다.. 풀이를 보고나니 생각보다 간단한 문젠데 못 풀어서 아쉬웠던 문제. 
</details> 
</blockquote></details> 
<details><summary> 2022.02.22 </summary><blockquote>
<details><summary> boj 1086, 박성원 </summary>
  
+ DP+비트마스크 문제. 먼저각각 숫자의 자릿수와 나머지를 저장해놓고, 그후 어떤숫자가 조합되었는지에 따라 bit와 나머지를 저장하는 DP테이블을 채워주면 된다. 처음에 DP를 채워가는 과정에서 TLE를 어떻게 해결해야 할까 고민 했었는데, 그냥 1부터 2^N까지 순서대로 채워도 문제가 없었다.<br> 그 이유가 더 높은 비트값은 반드시 이전의 비트값에 의해 갱신되므로 굳이 순서를 생각할 필요없이 1부터 순서대로 채워나가도 상관이 없었다.<br> 여러 아이디어를 떠올려야하는 문제였어서 풀기 쉽지 않았음.
</details> 
</blockquote></details> 
<details><summary> 2022.02.23 [!] </summary><blockquote>
  
+ 앞으로의 계획 : 전역까지 약 80일정도 남은 현 시점에서, PS이쯤에서 하고 일단 군대 전역까지는 내가 해보고 싶었던 프로젝트(플러터로 앱 만들기)를 해볼 예정입니다.<br> 물론 PS공부를 아예 쉴순 없으니, Python뿐만아니라 C/C++로 매일매일 쉬운 문제들로만 풀어볼 예정
</blockquote></details> 
  

  
</blockquote></details>  
  
<details><summary> 2022.03 </summary><blockquote>
<details><summary> 2022.03.04 </summary><blockquote>
<details><summary> boj 1915, 가장 큰 정사각형 </summary>

  + 오랜만에 DP문제를 풀어봤는데, 골드4치고 생각보다 빠르게 안풀려서 고민좀 했던 문제. <br>핵심은 DP테이블을 채워나가며 연속된 정사각형의 정보를 갱신하는데 있었음. 
</blockquote></details>  
<details><summary> 2022.03.26 </summary><blockquote>
<details><summary> boj 1013, Contact </summary>

  + 정규표현식말고 다른 풀이로도 풀어봐야겠다. 정규표현식을 모른 상태로 풀려니 어려웠음.
</blockquote></details>   
<details><summary> 2022.03.27 </summary><blockquote>
<details><summary> boj 3830, 교수님은 기다리지 않는다 </summary>

  + union find 응용문제로 생각하기 매우 어려웠음.<br> find 함수에서 부모를 갱신하는것외에 무게를 갱신해줘야하였음. union에서는 무게의 차를 갱신하여 더해주어야했음.
  
</blockquote></details> 
<details><summary> 2022.03.30 </summary><blockquote>
<details><summary> boj 1351, 무한수열 </summary>

  + 기본적인 DP문제.
</details>
<details><summary> boj 12904, A와 B </summary>

  + T->S 로 가는 역발상을 하여 풀면 쉬움. 매우쉽게 풀었음.
</blockquote></details>   
</blockquote></details> 
  
<details><summary> 2022.04 </summary><blockquote>
<details><summary> 2022.04.01 </summary><blockquote>
<details><summary> boj 1036, 36진수 </summary>

  + 간단한 구현문제. 반례때문에 한번 틀렸으니 다시보자.
</blockquote></details>  
<details><summary> 2022.04.03 </summary><blockquote>
<details><summary> boj 3190, 뱀 </summary>

  + 간단한 구현문젠데 자꾸 TLE가 나와서 고민해봤는데, direction을 설정할때 mod4연산을 안해줘서 반복문에서 무한루프로 TLE가 발생한거였음. 조심하자. 
</blockquote></details>  
<details><summary> 2022.04.05 </summary><blockquote>
<details><summary> boj 11689, GCD(n,k)=1 </summary>

  + sieve를 이용해 소수판정, 소인수분해, 그 후 백트래킹 까지 사용하여 풀었음. 다른사람들의 의견을 보니 오일러 파이 함수를 쓰는것으로 보아 정수론 공부를 더해야겠다 느낌. 다른 풀이도 찾아보자
  
</blockquote></details>
<details><summary> 2022.04.20 </summary><blockquote>
<details><summary> boj 2170, 선 긋기 </summary>

  + 스위핑 알고리즘 문제라길래 풀어봤는데, 스위핑을 쓰지않고 정렬후 간단한 아이디어로 풀리는 문제였다. 스위핑 알고리즘에 대해 공부해보자.
  
</blockquote></details>
<details><summary> 2022.04.21 </summary><blockquote>
<details><summary> boj 13334, 철로 </summary>

  + 스위핑 알고리즘 + PQ 문제. 매우 어려웠다. 우선순위큐를 떠올리지 못하였고, 스위핑 알고리즘 마저 제대로 알지못했음. <br>핵심 아이디어는 두번째 좌표로 오름차순 정렬후, 모든 주어진 구간값에 대해 PQ에 넣어주면서 반복문을 도는데, 이때 반드시 구간의 끝점이 커지므로 구간의 시작점도 커지므로 구간안에 들어가지 못하는 주어진 PQ내의 구간 값을 pop해주어야함. <br>그러므로 PQ의 길이가 바뀌면, 그때마다 PQ의 길이와 ans중 max값이 답이됨.
  
</blockquote></details>
<details><summary> 2022.04.26 </summary><blockquote>
<details><summary> boj 2064, IP 주소 </summary>

  + 이진수를 이용하는 구현문제. 반례찾기가 힘들어서 시간이 오래걸렸음.
</details>
<details><summary> boj 17298, 오큰수 </summary>

  + 스택을 이용해야한다는 아이디어를 떠올리기 쉽지않음. -> 스택을 떠올리면 풀기 쉬움.
</details>
</blockquote></details>
<details><summary> 2022.04.27 </summary><blockquote>
<details><summary> boj 1033, 칵테일 </summary>

  + 정수론+그래프 문제. <br>문제를 보자마자 풀이방법은 떠올랐으나, 그래프 탐색을 잘못구현하여 계속 WA를 받았음. 어디서 틀렸는지 다시 보자.
  
</blockquote></details>
  
</blockquote></details>

 
<details><summary> 2023.08 </summary><blockquote>
<details><summary> 2023.08.08 </summary><blockquote>
<details><summary> boj 18110, solved.ac </summary>

  + type error 로 고민했었는데, 이는 실수를 정수로 변환해주지 않아서 생긴문제였음.
  다음과 같이 s=s[t:len(s)-t] 를 리스트s에 슬라이싱을 사용할때 t는 정수여야함.
</blockquote></details>  

  
</blockquote></details>
  
</blockquote></details>
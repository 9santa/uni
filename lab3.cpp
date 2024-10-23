#include <bits/stdc++.h>
 
using namespace std;

using ll         =     long long;

#define F              first
#define S              second
#define pb             push_back
#define all(x)         x.begin(), x.end()
#define debug(x) cout << __FUNCTION__ << ":" << __LINE__ << " " << #x << " = " << x << endl
 
const int N = 1e5;
const int mod = 998244353;


vector<int> graph[N];
vector<bool> vis(N);
vector<bool> col(N);

bool flag = 0;

int razlom(int n,int m)
	{
		if (n == 1 && m == 1){
			return 0;
		}
		if (n == 1){
			return m-1;
		}
		if (m == 1){
			return n-1;
		}
		int ans = razlom((n+2-1)/2,m) + razlom(n-(n+2-1)/2,m) + 1;
		return ans;
	}

// void cohle()        
// {
// 	int n,m; cin >> n >> m;


// }
 
 
int main()
{
	// freopen("ancestor.in","rt",stdin);
	// freopen("ancestor.out","wt",stdout);
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	clock_t z = clock();
	
	int n,m; cin >> n >> m;
	cout << razlom(n,m);
	// cohle();

	
	// int t; cin >> t;
	// while(t--) cohle();
	
	cerr << "\nRun Time : " << ((double)(clock() - z) / CLOCKS_PER_SEC);
	
	system("pause");
	return 0;
}
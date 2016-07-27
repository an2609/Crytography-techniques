#include<bits/stdc++.h>
using namespace std;
int main()
{
	cout<<"Enter the string to be encrypted\n";
    char a[100000],b;
    cin.getline(a,100000);
    int n,k;
	cout<<"Enter the number of levels\n";
    cin>>n;
    fflush(stdin);
    int state[n]= {0};
    int l=strlen(a);
	cout<<"The encrypted string is\n";
    for(int i=0; i<l; i+=2*(n-1))
    {
        cout<<a[i];
    }
    for(int i=1; i<n-1; i++)
    {
        for(int j=i; j<l; j+=k)
        {
            if(state[i]==0)
            {
                k=2*(n-i-1);
                state[i]=1;
            }
            else
            {
                k=2*i;
                state[i]=0;
            }
            cout<<a[j];
        }
    }
    for(int i=n-1; i<l; i+=2*(n-1))
    {
        cout<<a[i];
    }
    cout<<endl;
    //cout<<n<<endl;
}

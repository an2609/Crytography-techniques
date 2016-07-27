#include<bits/stdc++.h>
using namespace std;
int main()
{
    char a[100000],b[100000];
    int n,k;
    cout<<"Enter the string to be decrypted\n";
    cin.getline(a,100000);
    cout<<"Enter the number of levels\n";
    cin>>n;
    int l=strlen(a),g;
    int i;
    for(i=0; i<l; i++)
    {
        g=i*2*(n-1);
        if(g>=l)
            break;
        b[g]=a[i];
    }
    for(int ii=1; ii<n-1; ii++)
    {
        int st=0;
        for(int j=ii; j<l; j+=k)
        {
            if(st==0)
            {
                b[j]=a[i++];
                k=2*(n-ii-1);
                if(k>=l)
                    break;
                st=1;
            }
            else
            {
                b[j]=a[i++];
                k=2*ii;
                if(k>=l)
                    break;
                st=0;
            }
        }
    }
    for(int ii=n-1; ii<l; ii+=2*(n-1))
    {
        b[ii]=a[i++];
    }
    cout<<"The decrypted string is\n";
    for(int i=0;i<l;i++)
        cout<<b[i];
    cout<<endl;
}


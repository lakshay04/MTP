#include<bits/stdc++.h>
using namespace std;
     
#define pb push_back
#define ll long long 
#define vl vector<long>
#define dob double
#define mp make_pair
#define fs first
#define se second
#define vp vector <pair<ll,ll> >
#define umap map<string, ll>

float DAMPING_FACTOR = 0.85;

   int Gauss_Southwell(vector<dob> *x,vector<dob> *r) {
         for(i=0;i<4;++i) {
            dob t=0;
            for(j=0;j<4;++j)
               t+=a*P[i][j];
            t+=(1-a)*b;
            x[i]=t;
            t=0;
            r[i]=x[i]-1;      
         }

         priority_queue <pair<dob,ll> > res;
         for(i=0;i<n;++i)
            res.push(mp((*r)[i],i));
         if(abs(res.top().fs)==0)
            return 0;
         else
         {
            (*x)[(res.top()).se]+=(res.top()).fs;
            (*r)[(res.top()).se]-=(res.top()).fs;
            for(i=0;i<n;++i)
               (*r)[i]+=A*(res.top()).fs*P[i][(res.top()).se];
            Gauss_Southwell(x,r);
         }
   }
   
   double initialValue(int N) {
      return 1/((double)N);
   }

    int main() {
      // getting no of vertices
      int N;
      cin >> N;

      // initial x
      vector<double> x(N);

      // initialise value of x
      int i;
      for (i = 0; i < N; i++) {
         x[i] = initialValue(N);
      }
      
      Gauss_Southwell(&x);

      return 0;
    }

    void trackingPpr(vector<dob> &xInitial) {
      vector<dob> x = xInitial;
      vector<dob> r(4);
      dob a=0.8,b=0.25,t=0;

      int i,j;
      // calculating r for every value
      for(i=0;i<4;++i)
      {
         t=0;
         for(j=0;j<4;++j)
            t+=a*P[i][j];
         t+=(1-a)*b;
         x[i]=t;
         r[i]=x[i]-1;      
      }

      Gauss_Southwell(&x, &r);

    }
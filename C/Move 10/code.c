void moveTen(char *str){
  
char arrn[] = "abcdefghijklmnopqrstuvwxyz";
char arrm[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

for (int i=0; i < strlen(str); i++)
  {
    int found = 0;
      for(int j= 0; j < 26; j++)
        {
          if (arrn[j] == str[i]){
             str[i] = arrn[(j+10) % 26];
               found = 1;
            break;
          }
      }
    if (found != 1){
      for(int j = 0; j < 26; j++)
        {
          if (arrm[j] == str[i]){
             str[i] = arrm[(j+10) % 26];
               found = 1;
            break;
          }
       }
    }
   }
}
#include <stdio.h>
#include <dirent.h>

int main(void)
{
  DIR *dirp;
  struct dirent *dp;
  dirp = opendir(".");

  while(1) {
    dp = readdir(dirp);
    if (dp == NULL)
    {
      puts("Directory reading completed.");
      break;
    }
    printf("%s\n", dp->d_name);
  }

  closedir(dirp);
}

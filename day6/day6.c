#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

// A structure to represent a queue 
struct Queue 
{ 
    int front, rear, size; 
    unsigned capacity; 
    int* array; 
}; 

int hash(char* name);
int intPower(int num, int power);
struct Queue* createQueue(unsigned capacity);
int isEmpty(struct Queue* queue);
void enqueue(struct Queue* queue, int item);
int dequeue(struct Queue* queue);

int main(int argc, char** argv)
{
    int lineCount = 0;
    int vertexCount = 0;
    int i, j;
    char line[9];
    int vertexIndices[363637];
    memset(line, '\0', 9);

    int fd = open("input.txt", O_RDONLY);
    int bytesRead = 0;
    int currentBytes = 0;

    do
    {
        char orbitedVertex[4], orbitingVertex[4];
        memset(orbitedVertex, '\0', 4);
        memset(orbitingVertex, '\0', 4);

        bytesRead = 0;

        while(bytesRead + (currentBytes = read(fd, line + bytesRead, 8 - bytesRead)) < 8 && currentBytes != 0)
            bytesRead += currentBytes;

        orbitedVertex[0] = line[0];
        orbitedVertex[1] = line[1];
        orbitedVertex[2] = line[2];

        orbitingVertex[0] = line[4];
        orbitingVertex[1] = line[5];
        orbitingVertex[2] = line[6];

        int orbitedHash = hash(orbitedVertex);
        int orbitingHash = hash(orbitingVertex);

        if(vertexIndices[orbitedHash] == 0)
        {
            vertexCount++;
            vertexIndices[orbitedHash] = vertexCount;
        }
        if(vertexIndices[orbitingHash] == 0)
        {
            vertexCount++;
            vertexIndices[orbitingHash] = vertexCount;
        }
    }while(currentBytes != 0);

    int** adjMatrix = (int**)malloc(vertexCount * sizeof(int*));
    for(i = 0; i < vertexCount; i++)
    {
        adjMatrix[i] = (int*)malloc(vertexCount * sizeof(int));
        for(j = 0; j < vertexCount; j++)
            adjMatrix[i][j] = 0;
    }

    lseek(fd, 0, SEEK_SET);

    do
    {
        char orbitedVertex[4], orbitingVertex[4];
        memset(orbitedVertex, '\0', 4);
        memset(orbitingVertex, '\0', 4);

        bytesRead = 0;

        while(bytesRead + (currentBytes = read(fd, line + bytesRead, 8 - bytesRead)) < 8 && currentBytes != 0)
            bytesRead += currentBytes;

        orbitedVertex[0] = line[0];
        orbitedVertex[1] = line[1];
        orbitedVertex[2] = line[2];

        orbitingVertex[0] = line[4];
        orbitingVertex[1] = line[5];
        orbitingVertex[2] = line[6];

        int orbitedHash = hash(orbitedVertex);
        int orbitingHash = hash(orbitingVertex);

        adjMatrix[vertexIndices[orbitedHash] - 1][vertexIndices[orbitingHash] - 1] = 1;
    }while(currentBytes != 0);

    int rootVertex = -1;
    int isRoot = 0;
    for(i = 0; i < vertexCount; i++)
    {
        for(j = 0; j < vertexCount; j++)
        {
            if(adjMatrix[j][i] == 1)
                break;
            if(j == vertexCount - 1)
                isRoot = 1;
        }

        if(isRoot)
        {
            rootVertex = i;
            break;
        }
    }

    int* visited = (int*)malloc(vertexCount*sizeof(int));
    int* shortestPath = (int*)malloc(vertexCount*sizeof(int));

    shortestPath[rootVertex] = 0;
    visited[rootVertex] = 1;
    
    struct Queue* queue = createQueue(vertexCount);
    enqueue(queue, rootVertex);

    while(!isEmpty(queue))
    {
        int currentVertex = dequeue(queue);
        for(i = 0; i < vertexCount; i++)
        {
            if(adjMatrix[currentVertex][i] == 1 && i != currentVertex && visited[i] == 0)
            {
                shortestPath[i] = shortestPath[currentVertex] + 1;
                enqueue(queue, i);
                visited[i] = 1;
            }
        }
    }

    int totalOrbits = 0;
    for(i = 0; i < vertexCount; i++)
    {
        totalOrbits += shortestPath[i];
    }

    printf("There are %d total orbits in the graph\n", totalOrbits);

    int youPlanet = -1;
    int santaPlanet = -1;

    for(i = 0; i < vertexCount; i++)
    {
        if(adjMatrix[i][vertexIndices[hash("YOU")] - 1] == 1)
            youPlanet = i;
        if(adjMatrix[i][vertexIndices[hash("SAN")] - 1] == 1)
            santaPlanet = i;
    }

    int youTransfers = 0;
    int santaTransfers = 0;

    while(shortestPath[youPlanet] > shortestPath[santaPlanet])
    {
        for(i = 0; i < vertexCount; i++)
        {
            if(adjMatrix[i][youPlanet] == 1)
            {
                youPlanet = i;
                youTransfers++;
                break;
            }
        }
    }

    while(shortestPath[santaPlanet] > shortestPath[youPlanet])
    {
        for(i = 0; i < vertexCount; i++)
        {
            if(adjMatrix[i][santaPlanet] == 1)
            {
                santaPlanet = i;
                santaTransfers++;
                break;
            }
        }
    }

    while(youPlanet != santaPlanet)
    {
        for(i = 0; i < vertexCount; i++)
        {
            if(adjMatrix[i][youPlanet] == 1)
            {
                youPlanet = i;
                youTransfers++;
                break;
            }
        }

        for(i = 0; i < vertexCount; i++)
        {
            if(adjMatrix[i][santaPlanet] == 1)
            {
                santaPlanet = i;
                santaTransfers++;
                break;
            }
        }
    }

    printf("There are %d orbital transfers required to move from YOU to SAN.\n", (youTransfers + santaTransfers));

    close(fd);
    for(i = 0; i < vertexCount; i++)
    {
        free(adjMatrix[i]);
    }
    free(adjMatrix);
    free(visited);
    free(shortestPath);
}

int hash(char* name)
{
    int j, k, result;
    k = 0;
    result = 0;

    for(j = strlen(name) - 1; j >= 0; j--)
    {
        if(name[j] >= '0' && name[j] <= '9')
            result += (name[j] - '0') * intPower(100, k);
        else if(name[j] >= 'A' && name[j] <= 'Z')
            result += (name[j] - 'A' + 10) * intPower(100, k);

        k++;
    }

    return result;
}

int intPower(int num, int power)
{
    int result = 1;
    while(power > 0)
    {
        result *= num;
        power--;
    }

    return result;
}

// function to create a queue of given capacity.  
// It initializes size of queue as 0 
struct Queue* createQueue(unsigned capacity) 
{ 
    struct Queue* queue = (struct Queue*) malloc(sizeof(struct Queue)); 
    queue->capacity = capacity; 
    queue->front = queue->size = 0;  
    queue->rear = capacity - 1;  // This is important, see the enqueue 
    queue->array = (int*) malloc(queue->capacity * sizeof(int)); 
    return queue; 
} 

int isEmpty(struct Queue* queue) 
{  return (queue->size == 0); } 
  
// Function to add an item to the queue.   
// It changes rear and size 
void enqueue(struct Queue* queue, int item) 
{
    queue->rear = (queue->rear + 1)%queue->capacity; 
    queue->array[queue->rear] = item; 
    queue->size = queue->size + 1; 
} 
  
// Function to remove an item from queue.  
// It changes front and size 
int dequeue(struct Queue* queue) 
{ 
    if (isEmpty(queue)) 
        return INT_MIN; 
    int item = queue->array[queue->front]; 
    queue->front = (queue->front + 1)%queue->capacity; 
    queue->size = queue->size - 1; 
    return item; 
} 
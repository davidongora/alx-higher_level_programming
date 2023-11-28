#ifndef LIST_H_
#define LIST_H_

typedef struct listint_t {
  int n;
  struct listint_t *next;
} listint_t;

listint_t *insert_node(listint_t **head, int number);
void print_list(listint_t *head);
void free_list(listint_t *head);

#endif

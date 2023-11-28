listint_t *insert_node(listint_t **head, int number) {
    listint_t *new_node = malloc(sizeof(listint_t));
    if (!new_node) {
        return NULL;
    }

    new_node->n = number;
    new_node->next = NULL;

    if (!*head) {
        *head = new_node;
        return new_node;
    }

    listint_t *prev = NULL;
    listint_t *curr = *head;

    while (curr && curr->n <= number) {
        prev = curr;
        curr = curr->next;
    }

    if (!prev) {
        new_node->next = *head;
        *head = new_node;
    } else {
        prev->next = new_node;
        new_node->next = curr;
    }

    return new_node;
}
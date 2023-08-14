#include "lists.h"
int is_palindrome(listint_t **head)
{
	while (*head->next != NULL)
	{
		printf("%d\n", *head->n);
		*head = *head->next;
	}
	return (0);
}

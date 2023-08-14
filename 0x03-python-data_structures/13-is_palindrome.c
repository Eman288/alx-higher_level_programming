#include "lists.h"
int is_palindrome(listint_t **head)
{
	listint_t *node = *head, *temp;

	int c, i, t;

	c = 0;
	i = 0;

	temp = node;
	while (temp != NULL)
	{
		c++;
		temp = temp->next;
	}
	t = c - i - 1;
	while (t > 0)
	{
		temp = node;
		while (t > 0)
		{
			temp = temp->next;
			t--;
		}
		if (node->n != temp->n)
			return (0);
		i += 2;
		t = c - i - 1;
		node = node->next;
	}
	return (1);
}

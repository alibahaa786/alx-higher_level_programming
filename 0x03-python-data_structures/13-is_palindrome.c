#include "lists.h"

/**
 * is_palindrome - check if linked list is a palindrome
 * @head: head node of linked list
 * Return: 1 if palindrome, else 0
*/

int is_palindrome(listint_t **head)
{
	int num = 0;
	int counter, j, i;
	listint_t *current, *compare;

	current = *head;
	if (!current)
		return (1);
	while (current)
	{
		num++;
		current = current->next;
	}
	for (i = 0; i < (num + 1) / 2; i++)
	{
		current = *head;
		compare = *head;
		for (j = 0; j < i; j++)
			current = current->next;
		counter = num - i - 1;
		while (counter--)
			compare = compare->next;
		if (current->n != compare->n)
			return (0);
	}
	return (1);
}

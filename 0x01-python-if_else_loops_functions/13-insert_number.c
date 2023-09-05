#include "lists.h"

/**
 * insert_node - function to insert node in a sorted list
 * @head: head node
 * @number: number to be added
 * Return: address of new node or NULL if failed
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new;
	listint_t *prev;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	if (current->n > new->n || !current)
	{
		new->next = current;
		*head = new;
		return (new);
	}
	prev = current;
	current = current->next;
	while (current)
	{
		if (current->n > new->n)
		{
			new->next = current;
			prev->next = new;
			return (new);
		}
		prev = current;
		current = current->next;
	}
	prev->next = new;
	new->next = NULL;
	return (new);
}

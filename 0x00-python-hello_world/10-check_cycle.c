#include "lists.h"

/**
 * check_cycle - check if linked list has a cycle
 * @list: head node of list
 * Return: 0 if there is no cycle, 1 if there is a cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *compare;
	while (list)
	{
		compare = list->next;
		while (compare)
		{
			if (compare->next == list)
				return (1);
			compare = compare->next;
		}
		list = list->next;
	}
	return (0);
}

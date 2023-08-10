/*
 * File: 10-check_cycle.c
 * Auth: Victorinox2
 */

#include "lists.h"

/**
 * check_cycle - checks if the linked list contains a cycle
 * @list: linked list to be checked
 *
 * Return: 1 if list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}

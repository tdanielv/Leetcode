# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Создаем два указателя, один на начало списка, другой на n узлов вперед
        dummy = ListNode(0)  # Создаем фиктивный узел в начале списка
        dummy.next = head
        first = dummy
        second = dummy

        # Перемещаем первый указатель на n узлов вперед
        for i in range(n + 1):
            first = first.next
            print(first)
        print('----')

        # Перемещаем первый и второй указатели одновременно до конца списка
        while first is not None:
            first = first.next
            second = second.next


        # Удаляем n-й узел, соединяя предыдущий и следующий узлы
        second.next = second.next.next

        # Возвращаем голову списка
        return dummy.next
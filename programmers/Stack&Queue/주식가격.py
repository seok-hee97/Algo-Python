def solution(prices):
  """
  주식 가격 변동에 따른 떨어지지 않은 기간 계산

  Args:
    prices: 초 단위로 기록된 주식 가격 배열

  Returns:
    각 가격 기준으로 떨어지지 않은 기간 리스트
  """

  answer = [len(prices)-i-1 for i in range(len(prices))]
  """
  초기화: 각 가격 기준 떨어지지 않은 기간은 마지막 인덱스까지 거리
  """

  for i in range(len(prices)):
    """
    현재 가격부터 마지막 가격까지 반복
    """
    for j in range(i+1, len(prices)):
      """
      현재 가격 다음 인덱스부터 마지막 인덱스까지 반복
      """
      if prices[i] > prices[j]:
        """
        현재 가격이 다음 가격보다 높으면 (가격이 떨어졌으면)
        """
        answer[i] = j-i
        """
        떨어지지 않은 기간을 현재 인덱스와 다음 인덱스의 차이로 설정
        """
        break
        """
        다음 인덱스를 확인할 필요 없으므로 루프 탈출
        """

  return answer
  """
  떨어지지 않은 기간 리스트 반환
  """

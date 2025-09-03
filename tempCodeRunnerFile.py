if cv2.waitKey(1) & 0xFF == ord("q"):
    pipeline.stop()   # يوقف البايبلاين
    cv2.destroyAllWindows()
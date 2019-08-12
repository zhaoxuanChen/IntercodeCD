; ModuleID = 'CWE121_Stack_Based_Buffer_Overflow__CWE193_wchar_t_alloca_ncpy_09.c'
source_filename = "CWE121_Stack_Based_Buffer_Overflow__CWE193_wchar_t_alloca_ncpy_09.c"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

@GLOBAL_CONST_TRUE = external constant i32, align 4
@CWE121_Stack_Based_Buffer_Overflow__CWE193_wchar_t_alloca_ncpy_09_bad.source = private unnamed_addr constant [11 x i32] [i32 65, i32 65, i32 65, i32 65, i32 65, i32 65, i32 65, i32 65, i32 65, i32 65, i32 0], align 16
@GLOBAL_CONST_FALSE = external constant i32, align 4
@.str = private unnamed_addr constant [21 x i8] c"Benign, fixed string\00", align 1
@goodG2B1.source = private unnamed_addr constant [11 x i32] [i32 65, i32 65, i32 65, i32 65, i32 65, i32 65, i32 65, i32 65, i32 65, i32 65, i32 0], align 16
@goodG2B2.source = private unnamed_addr constant [11 x i32] [i32 65, i32 65, i32 65, i32 65, i32 65, i32 65, i32 65, i32 65, i32 65, i32 65, i32 0], align 16

; Function Attrs: noinline nounwind optnone uwtable
define void @CWE121_Stack_Based_Buffer_Overflow__CWE193_wchar_t_alloca_ncpy_09_bad() #0 {
  %1 = alloca i32*, align 8
  %2 = alloca i32*, align 8
  %3 = alloca i32*, align 8
  %4 = alloca [11 x i32], align 16
  %5 = alloca i8, i64 40, align 16
  %6 = bitcast i8* %5 to i32*
  store i32* %6, i32** %2, align 8
  %7 = alloca i8, i64 44, align 16
  %8 = bitcast i8* %7 to i32*
  store i32* %8, i32** %3, align 8
  %9 = load i32, i32* @GLOBAL_CONST_TRUE, align 4
  %10 = icmp ne i32 %9, 0
  br i1 %10, label %11, label %15

; <label>:11:                                     ; preds = %0
  %12 = load i32*, i32** %2, align 8
  store i32* %12, i32** %1, align 8
  %13 = load i32*, i32** %1, align 8
  %14 = getelementptr inbounds i32, i32* %13, i64 0
  store i32 0, i32* %14, align 4
  br label %15

; <label>:15:                                     ; preds = %11, %0
  %16 = bitcast [11 x i32]* %4 to i8*
  call void @llvm.memcpy.p0i8.p0i8.i64(i8* %16, i8* bitcast ([11 x i32]* @CWE121_Stack_Based_Buffer_Overflow__CWE193_wchar_t_alloca_ncpy_09_bad.source to i8*), i64 44, i32 16, i1 false)
  %17 = load i32*, i32** %1, align 8
  %18 = getelementptr inbounds [11 x i32], [11 x i32]* %4, i32 0, i32 0
  %19 = getelementptr inbounds [11 x i32], [11 x i32]* %4, i32 0, i32 0
  %20 = call i64 @wcslen(i32* %19) #5
  %21 = add i64 %20, 1
  %22 = call i32* @wcsncpy(i32* %17, i32* %18, i64 %21) #6
  %23 = load i32*, i32** %1, align 8
  call void @printWLine(i32* %23)
  ret void
}

; Function Attrs: argmemonly nounwind
declare void @llvm.memcpy.p0i8.p0i8.i64(i8* nocapture writeonly, i8* nocapture readonly, i64, i32, i1) #1

; Function Attrs: nounwind
declare i32* @wcsncpy(i32*, i32*, i64) #2

; Function Attrs: nounwind readonly
declare i64 @wcslen(i32*) #3

declare void @printWLine(i32*) #4

; Function Attrs: noinline nounwind optnone uwtable
define void @CWE121_Stack_Based_Buffer_Overflow__CWE193_wchar_t_alloca_ncpy_09_good() #0 {
  call void @goodG2B1()
  call void @goodG2B2()
  ret void
}

; Function Attrs: noinline nounwind optnone uwtable
define internal void @goodG2B1() #0 {
  %1 = alloca i32*, align 8
  %2 = alloca i32*, align 8
  %3 = alloca i32*, align 8
  %4 = alloca [11 x i32], align 16
  %5 = alloca i8, i64 40, align 16
  %6 = bitcast i8* %5 to i32*
  store i32* %6, i32** %2, align 8
  %7 = alloca i8, i64 44, align 16
  %8 = bitcast i8* %7 to i32*
  store i32* %8, i32** %3, align 8
  %9 = load i32, i32* @GLOBAL_CONST_FALSE, align 4
  %10 = icmp ne i32 %9, 0
  br i1 %10, label %11, label %12

; <label>:11:                                     ; preds = %0
  call void @printLine(i8* getelementptr inbounds ([21 x i8], [21 x i8]* @.str, i32 0, i32 0))
  br label %16

; <label>:12:                                     ; preds = %0
  %13 = load i32*, i32** %3, align 8
  store i32* %13, i32** %1, align 8
  %14 = load i32*, i32** %1, align 8
  %15 = getelementptr inbounds i32, i32* %14, i64 0
  store i32 0, i32* %15, align 4
  br label %16

; <label>:16:                                     ; preds = %12, %11
  %17 = bitcast [11 x i32]* %4 to i8*
  call void @llvm.memcpy.p0i8.p0i8.i64(i8* %17, i8* bitcast ([11 x i32]* @goodG2B1.source to i8*), i64 44, i32 16, i1 false)
  %18 = load i32*, i32** %1, align 8
  %19 = getelementptr inbounds [11 x i32], [11 x i32]* %4, i32 0, i32 0
  %20 = getelementptr inbounds [11 x i32], [11 x i32]* %4, i32 0, i32 0
  %21 = call i64 @wcslen(i32* %20) #5
  %22 = add i64 %21, 1
  %23 = call i32* @wcsncpy(i32* %18, i32* %19, i64 %22) #6
  %24 = load i32*, i32** %1, align 8
  call void @printWLine(i32* %24)
  ret void
}

declare void @printLine(i8*) #4

; Function Attrs: noinline nounwind optnone uwtable
define internal void @goodG2B2() #0 {
  %1 = alloca i32*, align 8
  %2 = alloca i32*, align 8
  %3 = alloca i32*, align 8
  %4 = alloca [11 x i32], align 16
  %5 = alloca i8, i64 40, align 16
  %6 = bitcast i8* %5 to i32*
  store i32* %6, i32** %2, align 8
  %7 = alloca i8, i64 44, align 16
  %8 = bitcast i8* %7 to i32*
  store i32* %8, i32** %3, align 8
  %9 = load i32, i32* @GLOBAL_CONST_TRUE, align 4
  %10 = icmp ne i32 %9, 0
  br i1 %10, label %11, label %15

; <label>:11:                                     ; preds = %0
  %12 = load i32*, i32** %3, align 8
  store i32* %12, i32** %1, align 8
  %13 = load i32*, i32** %1, align 8
  %14 = getelementptr inbounds i32, i32* %13, i64 0
  store i32 0, i32* %14, align 4
  br label %15

; <label>:15:                                     ; preds = %11, %0
  %16 = bitcast [11 x i32]* %4 to i8*
  call void @llvm.memcpy.p0i8.p0i8.i64(i8* %16, i8* bitcast ([11 x i32]* @goodG2B2.source to i8*), i64 44, i32 16, i1 false)
  %17 = load i32*, i32** %1, align 8
  %18 = getelementptr inbounds [11 x i32], [11 x i32]* %4, i32 0, i32 0
  %19 = getelementptr inbounds [11 x i32], [11 x i32]* %4, i32 0, i32 0
  %20 = call i64 @wcslen(i32* %19) #5
  %21 = add i64 %20, 1
  %22 = call i32* @wcsncpy(i32* %17, i32* %18, i64 %21) #6
  %23 = load i32*, i32** %1, align 8
  call void @printWLine(i32* %23)
  ret void
}

attributes #0 = { noinline nounwind optnone uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { argmemonly nounwind }
attributes #2 = { nounwind "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #3 = { nounwind readonly "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #4 = { "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #5 = { nounwind readonly }
attributes #6 = { nounwind }

!llvm.module.flags = !{!0}
!llvm.ident = !{!1}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{!"clang version 6.0.0 (trunk 318634)"}
